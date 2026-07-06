import json
import os
import time
import urllib.request
from datetime import datetime, timezone

DEFAULT_TIMEOUT_S = 10


class PytestApiReporter:
    def __init__(self):
        self.start_time = None
        self.total = 0
        self.passed = 0
        self.failed = 0
        self.skipped = 0
        self.suites = set()
        self.failed_suites = set()
        self.failures = []

    def pytest_sessionstart(self, session):
        self.start_time = time.time()

    def pytest_runtest_logreport(self, report):
        node_file = str(report.fspath)

        if report.when == "call":
            self.suites.add(node_file)
            self.total += 1
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1
                self.failed_suites.add(node_file)
                first_line = str(report.longrepr).split("\n")[0]
                self.failures.append(f"{report.nodeid}: {first_line}")
            elif report.skipped:
                self.skipped += 1
        elif report.when == "setup":
            if report.skipped:
                self.total += 1
                self.skipped += 1
            elif report.failed:
                self.suites.add(node_file)
                self.failed_suites.add(node_file)

    def pytest_sessionfinish(self, session, exitstatus):
        api_url = os.environ.get("TEST_REPORT_API_URL")
        if not api_url:
            return

        finished_at = datetime.now(timezone.utc)
        duration_ms = int((time.time() - self.start_time) * 1000)

        total_suites = len(self.suites)
        failed_suites = len(self.failed_suites)
        passed_suites = total_suites - failed_suites
        status = "failed" if (self.failed > 0 or failed_suites > 0) else "passed"

        app = os.environ.get("TEST_REPORT_APP", "tollguru-api-parameter-examples")
        app_label = os.environ.get("TEST_REPORT_APP_LABEL", "TollGuru-API-Examples")
        environment = os.environ.get("TEST_REPORT_ENVIRONMENT") or ("ci" if os.environ.get("CI") else "local")
        repository = (
            os.environ.get("TEST_REPORT_REPOSITORY")
            or os.environ.get("GITHUB_REPOSITORY")
            or "tollguru-api-parameter-examples"
        )
        run_id = (
            os.environ.get("TEST_REPORT_RUN_ID")
            or os.environ.get("GITHUB_RUN_ID")
            or str(int(time.time()))
        )
        test_type = os.environ.get("TEST_REPORT_TEST_TYPE", "Pytest Integration")
        ci_run_url = self._build_ci_run_url()

        test_name = (
            f"{app} integration test summary: "
            f"{self.total} total, {self.passed} passed, "
            f"{self.failed} failed, {self.skipped} skipped"
        )
        failure_message = ""
        if status == "failed" and self.failures:
            failure_message = "\n".join(self.failures[:10])[:10_000]

        payload = {
            "runId": run_id,
            "finishedAt": finished_at.strftime("%Y-%m-%d %H:%M:%S"),
            "repository": repository,
            "app": app,
            "appLabel": app_label,
            "environment": environment,
            "testType": test_type,
            "browserRuntime": "python",
            "testName": test_name,
            "status": status,
            "durationMs": duration_ms,
            "source": "pytest",
            "failureMessage": failure_message,
            "ciRunUrl": ci_run_url,
            "coverage": "",
            "totalTestSuites": str(total_suites),
            "passedTestSuites": str(passed_suites),
            "failedTestSuites": str(failed_suites),
            "totalTest": str(self.total),
            "passedTest": str(self.passed),
            "failedTest": str(self.failed),
            "notifyOnPass": True,
        }

        self._post(api_url, payload)

    def _build_ci_run_url(self):
        override = os.environ.get("TEST_REPORT_CI_RUN_URL")
        if override:
            return override
        repo = os.environ.get("GITHUB_REPOSITORY")
        run_id = os.environ.get("GITHUB_RUN_ID")
        if repo and run_id:
            return f"https://github.com/{repo}/actions/runs/{run_id}"
        return ""

    def _post(self, api_url, payload):
        raw = os.environ.get("TEST_REPORT_TIMEOUT_MS")
        timeout_s = int(raw) // 1000 if raw and raw.isdigit() else DEFAULT_TIMEOUT_S
        fail_on_error = os.environ.get("TEST_REPORT_FAIL_ON_ERROR", "").lower() == "true"

        try:
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                api_url,
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=timeout_s) as resp:
                if resp.status >= 400:
                    raise RuntimeError(f"Report API returned {resp.status}")
        except Exception as exc:
            if fail_on_error:
                raise
            print(f"\n[pytest-api-reporter] Failed to send summary report: {exc}")

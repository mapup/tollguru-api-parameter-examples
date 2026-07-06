import json
import os
import re

import pytest
import requests

from tests.pytest_api_reporter import PytestApiReporter

BASE_URL = "https://apis.tollguru.com/toll/v2"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUEST_BODIES_DIR = os.path.join(ROOT_DIR, "request-bodies")


def load_json(path):
    """Load JSON tolerantly — strips trailing commas present in some request files."""
    with open(path) as f:
        text = f.read()
    text = re.sub(r",(\s*[}\]])", r"\1", text)
    return json.loads(text)


def pytest_configure(config):
    config.pluginmanager.register(PytestApiReporter(), "api-reporter")


@pytest.fixture(scope="session")
def api_key():
    key = os.environ.get("TOLLGURU_API_KEY")
    if not key:
        pytest.skip("Set TOLLGURU_API_KEY env var to run integration tests")
    return key


@pytest.fixture(scope="session")
def session(api_key):
    s = requests.Session()
    s.headers.update({"x-api-key": api_key})
    return s

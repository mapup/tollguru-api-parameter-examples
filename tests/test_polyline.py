import glob
import os

import pytest

from tests.conftest import BASE_URL, REQUEST_BODIES_DIR, load_json

ENDPOINT = f"{BASE_URL}/complete-polyline-from-mapping-service"
_req_dir = os.path.join(REQUEST_BODIES_DIR, "02-Complete-Polyline-To-Toll")


def _test_id(path):
    parts = path.split(os.sep)
    if "specify-vehicle-type" in parts:
        return f"specify-vehicle-type/{os.path.basename(path)}"
    return os.path.basename(path)


_base_files = sorted(glob.glob(os.path.join(_req_dir, "*.json")))
_vehicle_files = sorted(glob.glob(os.path.join(_req_dir, "specify-vehicle-type", "*.json")))
_files = _base_files + _vehicle_files


@pytest.mark.integration
@pytest.mark.parametrize("req_file", _files, ids=[_test_id(f) for f in _files])
def test_polyline(req_file, session):
    payload = load_json(req_file)

    resp = session.post(ENDPOINT, json=payload)

    assert resp.status_code == 200, f"HTTP {resp.status_code}: {resp.text[:300]}"
    data = resp.json()
    assert data.get("status") == "OK", f"Non-OK status: {data.get('status')} — {data}"
    assert "summary" in data, "Missing 'summary' key in response"
    # Polyline endpoint returns singular 'route', not 'routes'
    assert "route" in data, "Missing 'route' key in response"

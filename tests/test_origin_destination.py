import glob
import os

import pytest

from tests.conftest import BASE_URL, REQUEST_BODIES_DIR, load_json

ENDPOINT = f"{BASE_URL}/origin-destination-waypoints"
_req_dir = os.path.join(REQUEST_BODIES_DIR, "01-Origin-Destination-Cost-Tradeoff")
_files = sorted(glob.glob(os.path.join(_req_dir, "*.json")))


@pytest.mark.integration
@pytest.mark.parametrize("req_file", _files, ids=[os.path.basename(f) for f in _files])
def test_origin_destination(req_file, session):
    payload = load_json(req_file)

    resp = session.post(ENDPOINT, json=payload)

    assert resp.status_code == 200, f"HTTP {resp.status_code}: {resp.text[:300]}"
    data = resp.json()
    assert data.get("status") == "OK", f"Non-OK status: {data.get('status')} — {data}"
    assert "summary" in data, "Missing 'summary' key in response"
    assert "routes" in data, "Missing 'routes' key in response"
    assert isinstance(data["routes"], list) and len(data["routes"]) > 0, "routes must be non-empty list"

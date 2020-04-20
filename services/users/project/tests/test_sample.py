# services/users/project/tests/test_sample.py


import json


def test_sample(test_app):
    client = test_app.test_client()
    resp = client.get("/sample")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert "pong" in data["message"]
    assert "success" in data["status"]

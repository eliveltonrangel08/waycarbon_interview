from fastapi.testclient import TestClient


def test_get_access_token(client: TestClient) -> None:
    login_data = {
        "username": "test@test.com",
        "password": "mysimplepassword",
    }
    r = client.post("/api/v1/login/access-token", data=login_data)
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]


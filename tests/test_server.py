import pytest
from fastapi.testclient import TestClient

from vlmrun.hub.server.app import app
from vlmrun.hub.version import __version__


@pytest.fixture
def client():
    return TestClient(app)


def test_info(client):
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert data["version"] == __version__


def test_list_domains(client):
    response = client.get("/domains")
    assert response.status_code == 200
    domains = response.json()
    assert isinstance(domains, list)
    assert len(domains) > 0
    assert all(isinstance(d["domain"], str) for d in domains)


def test_has_domain(client):
    response = client.get("/domains/document.invoice")
    assert response.status_code == 200
    assert response.json() is True

    response = client.get("/domains/invalid.domain")
    assert response.status_code == 200
    assert response.json() is False


def test_get_schema_valid_domain(client):
    response = client.post("/schema", json={"domain": "document.invoice"})
    assert response.status_code == 200
    data = response.json()
    assert "json_schema" in data
    assert "schema_version" in data
    assert "schema_hash" in data


def test_get_schema_invalid_domain(client):
    response = client.post("/schema", json={"domain": "invalid.domain"})
    assert response.status_code == 404

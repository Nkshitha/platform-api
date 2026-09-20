import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status(client):
    r = client.get('/')
    assert r.status_code == 200

def test_home_payload(client):
    r = client.get('/')
    d = r.get_json()
    assert d['service'] == 'platform-api'
    assert d['status']  == 'running'
    assert 'version'    in d
    assert 'timestamp'  in d

def test_health_status(client):
    r = client.get('/health')
    assert r.status_code == 200

def test_health_payload(client):
    r = client.get('/health')
    d = r.get_json()
    assert d['healthy'] == True

def test_metrics_status(client):
    r = client.get('/metrics')
    assert r.status_code == 200

def test_metrics_payload(client):
    r = client.get('/metrics')
    d = r.get_json()
    assert 'service'     in d
    assert 'version'     in d
    assert 'environment' in d

def test_ready_status(client):
    r = client.get('/ready')
    assert r.status_code == 200

def test_ready_payload(client):
    r = client.get('/ready')
    d = r.get_json()
    assert d['ready'] == True

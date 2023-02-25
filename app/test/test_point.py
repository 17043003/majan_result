from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_kokushi_point():
    response = client.get('/point/kokushi')
    assert response.status_code == 200
    assert response.json()['cost']['total'] == 64000

def test_get_5200_point():
    query = '?m=112233&s=23466&p=234&w_p=2&dora_s=2&tsumo=True'
    response = client.get('/point/' + query)
    assert response.status_code == 200
    assert response.json()['cost']['total'] == 5200

def test_get_point():
    query = '?m=123'
    response = client.get('/point/' + query)
    assert response.status_code == 404

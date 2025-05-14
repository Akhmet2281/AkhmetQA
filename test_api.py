import requests

def test_status_code():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)
    assert response.status_code == 200
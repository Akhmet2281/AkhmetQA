import pytest
import requests

@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_multiple_posts(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == post_id


@pytest.mark.parametrize("invalid_id", [0, 9999, -1])
def test_invalid_post_id_returns_404(invalid_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{invalid_id}"
    response = requests.get(url)

    assert response.status_code == 404


def test_response_headers():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    # Проверяем, что в заголовках есть Content-Type и он application/json
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

def test_response_time():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    # Проверяем, что время ответа менее 500 мс
    assert response.elapsed.total_seconds() < 0.5

def test_json_structure():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    json_data = response.json()
    expected_keys = {"userId", "id", "title", "body"}
    
    # Проверяем, что все ключи есть в ответе
    assert expected_keys.issubset(json_data.keys())

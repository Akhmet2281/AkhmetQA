# tests/test_api.py
import requests

def test_api_status_code():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    # Проверка, что статус код 200 (успех)
    assert response.status_code == 200

def test_api_content():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    # Проверка содержимого (вместо 1 - проверим что именно у нас)
    json_data = response.json()
    assert json_data['id'] == 1
    assert json_data['title'] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"

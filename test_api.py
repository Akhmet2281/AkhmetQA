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

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_create_and_get_post():
    # 1. Создаём пост (POST-запрос)
    post_data = {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }
    response_post = requests.post(f"{BASE_URL}/posts", json=post_data)

    # Проверяем, что успешно создан (201)
    assert response_post.status_code == 201

    created_post = response_post.json()
    post_id = created_post.get("id")

    # 2. Получаем пост по ID (GET-запрос)
    response_get = requests.get(f"{BASE_URL}/posts/{post_id}")

    # Проверяем, что успешно получен (200)
    assert response_get.status_code == 200

    fetched_post = response_get.json()

    # 3. Проверяем, что данные совпадают
    assert fetched_post["title"] == post_data["title"]
    assert fetched_post["body"] == post_data["body"]
    assert fetched_post["userId"] == post_data["userId"]

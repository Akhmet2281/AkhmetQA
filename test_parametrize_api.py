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

import requests

BASE_URL = 'https://reqres.in/api'


def test_get_user():
    user_id = 2
    url = BASE_URL + f'/users/{user_id}'
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id


def test_put_user():
    user_id = 2
    url = BASE_URL + f'/users/{user_id}'
    response = requests.put(url)
    assert response.status_code == 200
    assert "updatedAt" in response.json()


def test_delete_user():
    user_id = 2
    url = BASE_URL + f'/users/{user_id}'
    response = requests.delete(url)
    assert response.status_code == 204


def test_post_user():
    data = {
        'email': 'ps@mail.com',
        'first_name': 'Pavel',
        'last_name': 'Svirin',
        'avatar': 'https://reqres.in/img/faces/2-image.jpg'
    }
    url = BASE_URL + f'/users/'
    response = requests.post(url, data=data)
    assert response.status_code == 201

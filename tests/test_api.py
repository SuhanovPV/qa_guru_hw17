import json
import requests
from jsonschema import validate
from qa_guru_hw17.utils import get_json_schema

BASE_URL = 'https://reqres.in/api'


def test_get_users():
    url = BASE_URL + '/users/'
    page = 2
    params = {'page': page}
    response = requests.get(url, params=params)
    print(response.json())
    assert response.status_code == 200
    validate(response.json(), get_json_schema.get_users_schema())
    assert response.json()['page'] == page


def test_put_user():
    user_id = 2
    url = BASE_URL + f'/users/{user_id}'
    response = requests.put(url)
    assert response.status_code == 200
    validate(response.json(), get_json_schema.get_user_update_schema())


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
    url = BASE_URL + '/users/'
    response = requests.post(url, data=data)
    assert response.status_code == 201
    validate(response.json(), get_json_schema.get_user_create_schema())


def test_get_exist_user():
    user_id = 2
    url = BASE_URL + f'/users/{user_id}'
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()['data']['id'] == 2


def test_get_nonexistent_user():
    user_id = 5356
    url = BASE_URL + f'/users/{user_id}'
    response = requests.get(url)
    assert response.status_code == 404
    assert any(response.json()) is False


def test_login_success_authorization():
    url = BASE_URL + "/login"
    data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(url, data=data)
    assert response.status_code == 200


def test_login_failure_authorization():
    url = BASE_URL + "/login"
    data = {"email": "ass@reqres.in", "password": "cityslicka"}
    response = requests.post(url, data=data)
    assert response.status_code == 400

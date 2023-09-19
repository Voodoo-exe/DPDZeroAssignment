import requests
import random

user_name = "test_user_{0}".format(random.randint(1, 1e6))
key_name = "test_key_{0}".format(random.randint(1, 1e6))

url = "http://localhost:5000"

def test_register_user():
    endpoint = "/api/register"
    data = {
        "username": user_name,
        "email": "{0}@example.com".format(user_name),
        "password": "test_password",
        "full_name": "Test User",
        "age": 30,
        "gender": "male"
    }
    response = requests.post(url + endpoint, json=data)
    print("response", response.request.url, response.request.method, response.status_code, response.text)
    assert response.status_code == 200
    assert response.json()["message"] == "User successfully registered!"

def test_generate_token():
    endpoint = "/api/token"
    data = {
        "username": user_name,
        "password": "test_password"
    }
    response = requests.post(url + endpoint, json=data)
    print("response", response.request.url, response.request.method, response.status_code, response.text)
    assert response.status_code == 200
    assert response.json()["message"] == "Access token generated successfully."
    return {"Authorization": "Bearer {0}".format(response.json()['data']['access_token'])}

def test_store_data():
    endpoint = "/api/data"
    data = {
        "key": key_name,
        "value": "test_value"
    }
    response = requests.post(url + endpoint, json=data, headers=test_generate_token())
    print("response", response.request.url, response.request.method, response.status_code, response.text)
    assert response.status_code == 200
    assert response.json()["message"] == "Data stored successfully."

def test_retrieve_data():
    endpoint = "/api/data/{0}".format(key_name)
    response = requests.get(url + endpoint, headers=test_generate_token())
    print("response", response.request.url, response.request.method, response.status_code, response.text)
    assert response.status_code == 200
    assert response.json()["data"]["key"] == key_name
    assert response.json()["data"]["value"] == "test_value"

def test_update_data():
    endpoint = "/api/data/{0}".format(key_name)
    data = {
        "value": "new_test_value"
    }
    response = requests.put(url + endpoint, json=data, headers=test_generate_token())
    print("response", response.request.url, response.request.method, response.status_code, response.text)
    assert response.status_code == 200
    assert response.json()["message"] == "Data updated successfully."

def test_delete_data():
    endpoint = "/api/data/{0}".format(key_name)
    response = requests.delete(url + endpoint, headers=test_generate_token())
    print("response", response.request.url, response.request.method, response.status_code, response.text)
    assert response.status_code == 200
    assert response.json()["message"] == "Data deleted successfully."

def test_all():
    test_register_user()
    test_generate_token()
    test_store_data()
    test_retrieve_data()
    test_update_data()
    test_delete_data()

if __name__ == "__main__":
    test_all()
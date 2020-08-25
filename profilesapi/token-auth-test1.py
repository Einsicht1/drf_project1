import requests

def client():
    token = "Token a09384e7bc4fbeca10a3b7431a87a56c6aee8ac8"
#    credentials = {'username': 'root', 'password' : '1234'}
#
#    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
#                            data=credentials)
    headers = {"authorization":token}
    response = requests.get("http://127.0.0.1:8000/api/profiles/",headers=headers)
    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()

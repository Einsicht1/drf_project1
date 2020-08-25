import requests
import json

def client():

#    data = {
#        "username" : "test",
#        "email" : "abc@gmail.com",
#        "password1" : "abcd1234zz",
#        "password2" : "abcd1234zz"
#    }
    token_h = 'Token 4b1e89c3127b3757ba6e24b9c20516629fda7e6c'
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)
    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()

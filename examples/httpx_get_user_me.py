import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string",
}

login_response = httpx.post(url="http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

me_headers = {"Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"}
me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=me_headers)
me_response_data = me_response.json()

print(me_response_data)
print(me_response.status_code)

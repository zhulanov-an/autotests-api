import httpx

headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.status_code)
print(response.request.headers)
# print(response.json())

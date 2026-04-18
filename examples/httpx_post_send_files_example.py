import httpx

with open("httpx_get_example.py", "rb") as f:
    files = {"file": ("example.txt", f)}
    response = httpx.post("https://httpbin.org/post", files=files)

print(response.status_code)
print(response.json())

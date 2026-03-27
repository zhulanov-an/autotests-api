import httpx

client = httpx.Client(http2=True)
response = client.get("https://www.google.com")

print(response.http_version)

client.close()
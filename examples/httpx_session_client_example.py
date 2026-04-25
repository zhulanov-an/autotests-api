from time import sleep

import httpx

with httpx.Client(headers={"Authorization": "Bearer my_secret_token"}) as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    sleep(5)
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())  # Данные первой задачи
print(response2.json())  # Данные второй задачи

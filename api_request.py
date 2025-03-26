import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

response = requests.get(f"{BASE_URL}/posts/1")

print(response.status_code)
print(response.json())

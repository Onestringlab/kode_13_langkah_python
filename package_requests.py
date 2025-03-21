import requests

response = requests.get("https://api.github.com")
print("Status Kode:", response.status_code)
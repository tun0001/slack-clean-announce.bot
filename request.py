import requests

url = "http://localhost:8000/callback"
data = {
    "events": [
        {"message": {"text": "こんにちは"}}
    ]
}

response = requests.post(url, json=data)
print("ステータス:", response.status_code)
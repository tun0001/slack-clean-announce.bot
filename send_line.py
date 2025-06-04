import requests
import os

ACCESS_TOKEN = os.environ["LINE_ACCESS_TOKEN"]
USER_ID = os.environ["LINE_USER_ID"]

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

data = {
    "to": USER_ID,
    "messages": [
        {
            "type": "text",
            "text": "✅ GitHub Actions からLINEに通知が届きました！"
        }
    ]
}

response = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=data)

if response.status_code == 200:
    print("✅ LINE送信成功")
else:
    print("❌ LINE送信失敗:", response.text)
import requests
import os

ACCESS_TOKEN = os.environ["LINE_ACCESS_TOKEN"]
USER_ID = os.environ["LINE_USER_ID"]

# 天気API
city_code = "270000"  # 大阪市
weather_url = f"https://weather.tsukumijima.net/api/forecast/city/{city_code}"
response = requests.get(weather_url)
data = response.json()

# メッセージ組み立て
title = data["title"]
forecasts = data["forecasts"]

msg = f"📍 {title}\n"
for f in forecasts:
    day = f["dateLabel"]
    telop = f["telop"]
    min_temp = f["temperature"]["min"]["celsius"] or "?"
    max_temp = f["temperature"]["max"]["celsius"] or "?"
    msg += f"{day}: {telop} 🌡️{min_temp}〜{max_temp}℃\n"

# LINE送信
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {LINE_TOKEN}"
}
data = {
    "to": USER_ID,
    "messages": [{"type": "text", "text": msg}]
}
r = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=data)
print("✅ LINE送信" if r.status_code == 200 else f"❌ 失敗: {r.text}")
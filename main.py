import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from slack_sdk import WebClient

# Google Sheets 認証
creds_json = json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"])
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
client = gspread.authorize(creds)

# スプレッドシートからデータ取得
sheet = client.open("YourSpreadsheetName").sheet1
records = sheet.get_all_records()

# Slack メッセージ整形
message = "*今週の報告*\n"
for row in records[-5:]:  # 最新の5件
    message += f"- {row['日付']}: {row['内容']}\n"

# Slack 投稿
slack_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = WebClient(token=slack_token)
slack_client.chat_postMessage(channel="#cream_remind", text=message)
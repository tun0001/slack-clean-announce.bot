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

sheet_id = "1y--2Lzvpgk8O7MlgBUZiLJq0LKIoglfNWaBG_bHfynk"
sheet = client.open_by_key(sheet_id).sheet1  # 1番目のシートを取得
# スプレッドシートからデータ取得
#sheet = client.open("YourSpreadsheetName").sheet1
cell_value1 = sheet.acell("G8").value
cell_value2 = sheet.acell("G9").value
print(cell_value1, cell_value2)
#records = sheet.get_all_records()
message = f"今週の報告: {cell_value1} - {cell_value2}"
# # Slack メッセージ整形
# message = "*今週の報告*\n"
# for row in records[-5:]:  # 最新の5件
#     message += f"- {row['日付']}: {row['内容']}\n"

# Slack 投稿
slack_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = WebClient(token=slack_token)
slack_client.chat_postMessage(channel="#clean_remind", text=message)
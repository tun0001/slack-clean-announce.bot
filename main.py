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

sheet_id = ""
sheet = client.open_by_key(sheet_id).sheet1  # 1番目のシートを取得
# スプレッドシートからデータ取得
#sheet = client.open("YourSpreadsheetName").sheet1
cleen_date = sheet.acell("C8:C9").value
D455_1 = sheet.acell("G8").value
D455_2 = sheet.acell("G9").value
experiment_1 = sheet.acell("I8").value
experiment_2 = sheet.acell("I9").value
F322_1 = sheet.acell("K8").value
F322_2 = sheet.acell("K9").value
H402_1 = sheet.acell("M8").value
H402_2 = sheet.acell("M9").value


name_id_dict = {"日高": "@f.hidaka", "佐々木": "@j.sasaki", "岩本": "@k.iwamoto", "野村":"@k.nomura", "甲斐野": "@s.kaino", "山田": "@y.yamada", 
            "Li": "@s.li", "福田": "@t.fukuda", "柳田": "@k.yanagida", "徳永": "@t.tokunaga", "木下": "@y.kinoshita", "小林": "@t.kobayashi",
           "服部": "@h.hattori", "加藤": "@t.kato", "伊藤": "@k.ito", "岡部": "@a.okabe", "尾崎": "@m.ozaki", "手代木": "@m.teshirogi", "森山": "@h.moriyama", "矢端": "@h.yabata"}

#print(cell_value1, cell_value2)
#records = sheet.get_all_records()
message = f"【{cleen_date}掃除連絡】\nD455:  {name_id_dict[D455_1]}  {name_id_dict[D455_2]}\n実験室:  {name_id_dict[experiment_1]}  {name_id_dict[experiment_2]} \nF322:  {name_id_dict[F322_1]}  {name_id_dict[F322_2]}\nH402(New): {name_id_dict[H402_1]} {name_id_dict[H402_2]}\n\n・掃除・ゴミ出し一回ごとに日付を記入\nhttps://docs.google.com/spreadsheets/d/1y--2Lzvpgk8O7MlgBUZiLJq0LKIoglfNWaBG_bHfynk/edit?gid=343667719#gid=343667719\n\n・所要時間が30分を超える場合は30分毎に日付を記入(例：1h15minなら3回日付を記入)\n・二人分掃除を行った場合は，二回分記入してください．\n・掃除後はsoro_cleanに作業者名を明記の上完了報告\n・研究室のためのボランティア作業(棚の組み立て等)も記入可能"
# # Slack メッセージ整形
# message = "*今週の報告*\n"
# for row in records[-5:]:  # 最新の5件
#     message += f"- {row['日付']}: {row['内容']}\n"

# Slack 投稿
slack_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = WebClient(token=slack_token)
slack_client.chat_postMessage(channel="#clean_remind", text=message)
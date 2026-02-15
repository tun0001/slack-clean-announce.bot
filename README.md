# slack-clean-announce.bot

Google Sheetsの掃除当番情報を取得し、Slackチャネルに自動投稿するボットです。

## 概要

このボットは以下の機能を提供します：

- Google Sheetsから掃除当番のデータを定期的に取得
- 担当者の名前をSlack IDに変換
- 掃除内容と担当者情報をSlack（#clean_remindチャネル）に自動投稿
- 掃除報告のためのスプレッドシートリンクを含む

## 必要な環境

- Python 3.7以上
- 環境変数：
  - `GOOGLE_CREDENTIALS_JSON`: Google Sheets APIの認証情報（JSON形式）
  - `SLACK_BOT_TOKEN`: SlackボットのAPIトークン

## インストール

```bash
pip install -r requirements.txt
```

## 依存ライブラリ

- `gspread`: Google Sheets APIとのやり取り
- `oauth2client`: Google Sheets認証
- `slack_sdk`: Slack APIとのやり取り

## 使用方法

```bash
python main.py
```

## 設定

Google Sheetsのスプレッドシートサンプルは以下の構成です：

| 項目 | セル | 説明 |
|------|------|------|
| 掃除日 | C8:C9 | 掃除予定日 |
| D455 | G8:G9 | D455室の担当者 |
| 実験室 | I8:I9 | 実験室の担当者 |
| F322 | K8:K9 | F322室の担当者 |
| H402 | M8:M9 | H402室の担当者 |

担当者名はスプレッドシート上の名前で、コード内の`name_id_dict`でSlack IDに変換されます。

## メッセージ形式

Slackに投稿されるメッセージ例：

```
【X月X日掃除連絡】
D455:  @user1  @user2
実験室:  @user3  @user4
F322:  @user5  @user6
H402(New): @user7 @user8

・掃除・ゴミ出し一回ごとに日付を記入
[スプレッドシートリンク]

・所要時間が30分を超える場合は30分毎に日付を記入(例：1h15minなら3回日付を記入)
・二人分掃除を行った場合は，二回分記入してください．
・掃除後はsoro_cleanに作業者名を明記の上完了報告
・研究室のためのボランティア作業(棚の組み立て等)も記入可能
```

## ライセンス

MIT
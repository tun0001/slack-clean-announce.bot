from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world!"

@app.route("/callback", methods=["POST"])
def callback():
    data = request.get_json()
    print("Webhook受信:", data)
    return "OK"

if __name__ == "__main__":
    app.run(port=8000)
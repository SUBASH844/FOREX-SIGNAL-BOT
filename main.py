import requests
from flask import Flask, request
import os

app = Flask(__name__)

# === Telegram Config ===
TOKEN = "7936050560:AAGs0jClA9wHlAqv3KthhfqCq-wxnhUcB3Yyo"
CHAT_ID = "7584202552"

@app.route('/signal', methods=['POST'])
def send_signal():
    data = request.json
    pair = data.get("pair")
    entry = data.get("entry")
    sl = data.get("sl")
    tp1 = data.get("tp1")
    tp2 = data.get("tp2")
    tp3 = data.get("tp3")
    tp4 = data.get("tp4")

    message = f"""
📉 *{pair} Signal* 📈

📍 Entry: {entry}
⛔ SL: {sl}
🎯 TP1: {tp1}
🎯 TP2: {tp2}
🎯 TP3: {tp3}
🎯 TP4: {tp4}
"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)
    return "OK", 200

@app.route('/')
def home():
    return "Bot is running"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

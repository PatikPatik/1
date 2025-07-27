from flask import Flask, request
import sqlite3
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
CRYPTOBOT_TOKEN = os.getenv("CRYPTOBOT_TOKEN")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

app = Flask(__name__)

# Telegram handler
@app.route(f"/{WEBHOOK_SECRET}", methods=["POST"])
def telegram_webhook():
    data = request.json
    # Обработка апдейтов Telegram, если нужно
    return "ok"

# CryptoBot handler
@app.route("/cryptobot", methods=["POST"])
def cryptobot_webhook():
    data = request.json
    # Обработка оплаты от CryptoBot
    # Например: проверка status == "paid", invoice_id и user_id
    return "ok"

@app.route("/")
def index():
    return "Bot is alive!"

if __name__ == "__main__":
    app.run()

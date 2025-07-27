from flask import Flask, request
import sqlite3
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
CRYPTOBOT_TOKEN = os.getenv("CRYPTOBOT_TOKEN")

# === Telegram webhook ===
@app.route(f"/{WEBHOOK_SECRET}", methods=["POST"])
def telegram_webhook():
    update = request.json
    # Здесь можно обрабатывать Telegram-апдейты, если нужно
    return "ok"

# === CryptoBot webhook ===
@app.route("/cryptobot", methods=["POST"])
def cryptobot_webhook():
    data = request.json
    if data.get("status") == "paid":
        user_id = data.get("user_id")
        amount = float(data.get("amount", 0))
        purchased_ths = amount / 13.7

        conn = sqlite3.connect("mining.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET balance = balance + ?, hashrate = hashrate + ? WHERE user_id = ?",
                       (amount, purchased_ths, user_id))

        cursor.execute("SELECT referrer_id FROM users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        if result and result[0]:
            referrer_id = result[0]
            bonus = amount * 0.01
            cursor.execute("UPDATE users SET balance = balance + ?, ref_bonus = ref_bonus + ? WHERE user_id = ?",
                           (bonus, bonus, referrer_id))

        conn.commit()
        conn.close()
    return "ok"

@app.route("/")
def index():
    return "Bot is alive!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

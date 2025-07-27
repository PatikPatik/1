Инструкция:
1. Создай репозиторий на GitHub и залей туда эти файлы.
2. Подключи репозиторий в Render как Web Service.
3. Укажи переменные окружения:
   - BOT_TOKEN — токен Telegram-бота
   - CRYPTOBOT_TOKEN — токен CryptoBot
   - WEBHOOK_SECRET — уникальный путь (например, a1b2c3)
4. Установи Webhook в Telegram на:
   https://<твой-домен>.onrender.com/<WEBHOOK_SECRET>
5. Установи Webhook в CryptoBot на:
   https://<твой-домен>.onrender.com/cryptobot

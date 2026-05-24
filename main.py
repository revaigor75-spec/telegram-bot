from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
import re
import asyncio

# =========================
# TELEGRAM API
# =========================
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION")

# =========================
# ID
# =========================
SOURCE_CHAT_ID = -1002155298579
TARGET_CHANNEL = -1003900818213

# =========================
# КЛЮЧЕВЫЕ СЛОВА
# =========================
KEYWORDS = ["rare", "epic", "legendary", "unique"]

# =========================
# CLIENT
# =========================
client = TelegramClient(
    StringSession(session_string),
    api_id,
    api_hash,
    auto_reconnect=True,
    retry_delay=5,
    connection_retries=None
)

# =========================
# ОБРАБОТКА СООБЩЕНИЙ
# =========================
@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def handler(event):
    try:
        text = event.raw_text
        print("НОВОЕ СООБЩЕНИЕ:", text)

        if not text:
            return

        text_lower = text.lower()
        duck_type = None

        for word in KEYWORDS:
            if word in text_lower:
                duck_type = word.upper()
                break

        if not duck_type:
            return

        # Поиск ссылки
        links = re.findall(r'(https?://\S+|t\.me/\S+)', text)
        if not links:
    print("ССЫЛКА НЕ НАЙДЕНА")
    return
        link = links[0]

        # Поиск названия
        duck_name = None
        lines = text.split("\n")
        for line in lines:
            line = line.strip()
            if len(line) > 3 and "http" not in line.lower() and "t.me" not in line.lower():
                if any(word in line.lower() for word in KEYWORDS):
                    duck_name = line
                    break

        if not duck_name:
            duck_name = f"{duck_type} DUCK"

        # Отправка в канал
        message = (
            f"🦆 <b>{duck_type} DUCK</b>\n\n"
            f"🏷 <b>{duck_name}</b>\n\n"
            f"🔗 {link}"
        )

        await client.send_message(TARGET_CHANNEL, message, parse_mode="html")
        print(f"✅ Отправлено: {duck_type} - {duck_name}")

    except Exception as e:
        print(f"ERROR: {e}")

# =========================
# MAIN
# =========================
async def main():
    print("🔄 Подключаемся к Telegram...")
    await client.connect()

    if await client.is_user_authorized():
        me = await client.get_me()
        print(f"✅ Userbot успешно запущен как: {me.first_name} (@{me.username})")
    else:
        print("❌ Сессия не авторизована! Нужно перелогиниться.")
        return

    print("🦆 DUCK USERBOT ЗАПУЩЕН И РАБОТАЕТ")
    await client.run_until_disconnected()

asyncio.run(main())
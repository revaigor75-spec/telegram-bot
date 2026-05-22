from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
import re
import asyncio

# =========================
# TELEGRAM API
# =========================

api_id = int(os.getenv("38572833"))
api_hash = os.getenv("f4e6a33ec52ba76cac20c1deefd37a26")

# SESSION STRING из Railway Variables
SESSION = os.getenv("SESSION")

# =========================
# ID
# =========================

# Группа откуда брать сообщения
SOURCE_CHAT_ID = -1002155298579

# Твой канал
TARGET_CHANNEL = -1003900818213

# =========================
# КЛЮЧЕВЫЕ СЛОВА
# =========================

KEYWORDS = [
    "rare",
    "epic",
    "legendary",
    "unique"
]

# =========================
# CLIENT
# =========================

client = TelegramClient(
    StringSession(SESSION),
    api_id,
    api_hash,
    auto_reconnect=True,
    retry_delay=5,
    connection_retries=None
)

# =========================
# ОБРАБОТКА СООБЩЕНИЙ
# =========================

@client.on(events.NewMessage)
async def handler(event):

    try:

        print("==========")
        print("НОВОЕ СООБЩЕНИЕ")
        print("CHAT ID:", event.chat_id)
        print("TEXT:", event.raw_text)

    except Exception as e:
        print("ERROR:", e)

# =========================
# MAIN LOOP
# =========================

async def main():

    print("DUCK USERBOT STARTED 🦆")

    await client.start()

    await client.run_until_disconnected()

while True:

    try:
        asyncio.run(main())

    except Exception as e:

        print("RECONNECT:", e)
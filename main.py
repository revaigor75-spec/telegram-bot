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

        if not text:
            return

        text_lower = text.lower()

        duck_type = None

        if "rare" in text_lower:
            duck_type = "🟢 RARE"
        elif "epic" in text_lower:
            duck_type = "🟣 EPIC"
        elif "legendary" in text_lower:
            duck_type = "🟡 LEGENDARY"
        elif "unique" in text_lower:
            duck_type = "🔴 UNIQUE"

        if not duck_type:
            return

        # Ищем ссылку
        links = re.findall(r'(https?://\S+|t\.me/\S+)', text)

        if not links:
            return

        link = links[0]

        # Сообщение в канал
        msg = f"{duck_type}\n\n🔗 {link}"

        await client.send_message(
            TARGET_CHANNEL,
            msg
        )

        print(f"ОТПРАВЛЕНО: {duck_type} | {link}")

    except Exception as e:
        print(f"ERROR: {e}")

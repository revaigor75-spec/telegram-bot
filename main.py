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

@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def handler(event):

    try:

        text = event.raw_text

        if not text:
            return

        text_lower = text.lower()

        duck_type = None

        # Ищем тип утки
        for word in KEYWORDS:

            if word in text_lower:
                duck_type = word.upper()
                break

        if not duck_type:
            return

        # Ищем ссылку
        links = re.findall(
            r'(https?://\S+|t\.me/\S+)',
            text
        )

        if not links:
            return

        link = links[0]

        # Ищем название утки
        duck_name = None

        lines = text.split("\n")

        for line in lines:

            line = line.strip()

            if (
                len(line) > 2
                and "http" not in line
                and "t.me/" not in line
            ):

                if any(
                    word in line.lower()
                    for word in KEYWORDS
                ):

                    duck_name = line
                    break

        if not duck_name:
            duck_name = f"{duck_type} DUCK"

        # Сообщение в канал
        message = (
            f"🦆 <b>{duck_type} DUCK</b>\n\n"
            f"🏷 <b>{duck_name}</b>\n\n"
            f"🔗 {link}"
        )

        await client.send_message(
            TARGET_CHANNEL,
            message,
            parse_mode="html"
        )

        print("ОТПРАВЛЕНО:")
        print(message)

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
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
import re

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")

SOURCE_CHAT_ID = -1002155298579
TARGET_CHANNEL = -1003900818213

client = TelegramClient(
    StringSession(SESSION),
    API_ID,
    API_HASH
)

print("USERBOT успешно запущен")


@client.on(events.NewMessage)
async def handler(event):
    try:
        text = event.raw_text

        print("СООБЩЕНИЕ ПОЛУЧЕНО")
        print("CHAT ID:", event.chat_id)
        print("TEXT:", text)

    except Exception as e:
        print("ERROR:", e)

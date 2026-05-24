from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")

client = TelegramClient(
    StringSession(SESSION),
    API_ID,
    API_HASH
)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    print("СООБЩЕНИЕ ПРИШЛО")
    print("CHAT:", event.chat_id)
    print("TEXT:", event.raw_text)

client.start()

print("БОТ ЗАПУЩЕН")

client.run_until_disconnected()

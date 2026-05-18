from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import asyncio

api_id = 36239085
api_hash = "963590c1d6bdcc8dc6995fb6b01aee1f"

client = TelegramClient(StringSession(), api_id, api_hash)

async def main():
    await client.start()
    print("BOT STARTED")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())

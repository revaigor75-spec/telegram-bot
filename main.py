from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.errors import PersistentTimestampOutdatedError

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

print("БОТ ЗАПУСКАЕТСЯ...")


@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def handler(event):
    try:
        text = event.raw_text

        print("СООБЩЕНИЕ:", text)

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

        links = re.findall(r'(https?://\S+|t\.me/\S+)', text)

        if not links:
            print("ССЫЛКА НЕ НАЙДЕНА")
            return

        link = links[0]

        msg = f"{duck_type}\n\n🔗 {link}"

        await client.send_message(
            TARGET_CHANNEL,
            msg
        )

        print("ОТПРАВЛЕНО В КАНАЛ")

    except PersistentTimestampOutdatedError:
        print("Telegram временно лагает")

    except Exception as e:
        print("ERROR:", e)


client.start()

print("БОТ ЗАПУЩЕН И РАБОТАЕТ")

client.run_until_disconnected()

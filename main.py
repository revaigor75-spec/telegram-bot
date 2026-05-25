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

        # =========================
        # ПОЛУЧАЕМ ТЕКСТ
        # =========================

        text = ""

        if event.message.message:
            text += event.message.message

        if event.message.raw_text:
            text += "\n" + event.message.raw_text

        text = text.strip()

        print("СООБЩЕНИЕ:", text)

        if not text:
            return

        text_lower = text.lower()

        # =========================
        # ИЩЕМ ТИП УТКИ
        # =========================

        duck_type = None

        if re.search(r'rare', text_lower):
            duck_type = "🟢 RARE"

        elif re.search(r'epic', text_lower):
            duck_type = "🟣 EPIC"

        elif re.search(r'legendary', text_lower):
            duck_type = "🟡 LEGENDARY"

        elif re.search(r'unique', text_lower):
            duck_type = "🔴 UNIQUE"

        # если нет типа утки — пропускаем
        if not duck_type:
            return

        # =========================
        # ИЩЕМ ВСЕ ССЫЛКИ
        # =========================

        links = re.findall(
            r'(https?://[^\s]+|t\.me/[^\s]+)',
            text
        )

        if not links:
            print("ССЫЛКИ НЕ НАЙДЕНЫ")
            return

        # =========================
        # СОБИРАЕМ ССЫЛКИ
        # =========================

        links_text = "\n".join(links)

        # =========================
        # СОБИРАЕМ СООБЩЕНИЕ
        # =========================

        msg = (
            f"{duck_type}\n\n"
            f"🔗 {links_text}"
        )

        # =========================
        # ОТПРАВЛЯЕМ
        # =========================

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

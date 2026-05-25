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

        # =========================
        # ИЩЕМ НАЗВАНИЕ УТКИ
        # =========================

        if "rare" in text_lower:
            duck_type = "🟢 RARE"

        elif "epic" in text_lower:
            duck_type = "🟣 EPIC"

        elif "legendary" in text_lower:
            duck_type = "🟡 LEGENDARY"

        elif "unique" in text_lower:
            duck_type = "🔴 UNIQUE"

        # если нет названия — пропускаем
        if not duck_type:
            return

        # =========================
        # ИЩЕМ ССЫЛКИ
        # =========================

        links = re.findall(
            r'(https?://[^\s]+|t\.me/[^\s]+)',
            text
        )

        if not links:
            print("ССЫЛКА НЕ НАЙДЕНА")
            return

        # =========================
        # УДАЛЯЕМ ДУБЛИ
        # =========================

        links = list(dict.fromkeys(links))

        # берём только первую ссылку
        link = links[0]

        # =========================
        # СОБИРАЕМ СООБЩЕНИЕ
        # =========================

        msg = f"{duck_type}\n\n🔗 {link}"

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

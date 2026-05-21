from telethon import TelegramClient, events
import re

api_id = 38572833
api_hash= "f4e6a33ec52ba76cac20c1deefd37a26"

SOURCE_CHAT_NAME = "DUCK × MY × DUCK | Duckers group"
TARGET_CHANNEL = -1003900818213

KEYWORDS = ["rare", "epic"]

client = TelegramClient("duck_new_session", api_id, api_hash)


@client.on(events.NewMessage)
async def handler(event):

    chat = await event.get_chat()

    if getattr(chat, "title", "") != SOURCE_CHAT_NAME:
        return

    text = event.raw_text.lower()

    print("Новое сообщение:")
    print(text)

    # ссылка
    link_match = re.search(r'https?://\S+', text)

    if not link_match:
        return

    link = link_match.group(0)

    result = None

    # ищем rare / epic + число
    for word in KEYWORDS:

        pattern = rf'\b{word}\b\s*([1-4])?'

        match = re.search(pattern, text)

        if match:

            level = match.group(1)

            if level:
                result = f"{word} {level}"
            else:
                result = word

            break

    if not result:
        return

    final_message = f"{result}\n{link}"

    await client.send_message(
        TARGET_CHANNEL,
        final_message,
        link_preview=False
    )

    print("Отправлено:")
    print(final_message)


print("Бот запущен")

client.start()
client.run_until_disconnected()
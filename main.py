from telethon import TelegramClient, events
import re

api_id = 38572833
api_hash= "f4e6a33ec52ba76cac20c1deefd37a26"

SOURCE_CHAT_ID = -1002155298579
TARGET_CHANNEL = -1003900818213

KEYWORDS = ["rare", "epic"]

client = TelegramClient("duck_new_session", api_id, api_hash)


@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def handler(event):

    text = event.raw_text

    if not text:
        return

    print("Получено сообщение:")
    print(text)

    import re

    links = re.findall(
        r'(https?://\S+|t\.me/\S+)',
        text
    )

    if not links:
        return

    text_lower = text.lower()

    duck_type = None

    if "rare" in text_lower:
        duck_type = "RARE"

    elif "epic" in text_lower:
        duck_type = "EPIC"

    if not duck_type:
        return

    message = (
        f"🦆 {duck_type} DUCK\n\n"
        f"🔗 {links[0]}"
    )

    await client.send_message(
        TARGET_CHANNEL,
        message
    )

    print("Отправлено в канал")
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

    text = event.raw_text

    if not text:
        return

    text_lower = text.lower()

    found_word = None

    for word in KEYWORDS:
        if word in text_lower:
            found_word = word.upper()
            break

    if not found_word:
        return

    import re

    links = re.findall(
        r'(https?://\S+|t\.me/\S+)',
        text
    )

    if not links:
        return

    link = links[0]

    message = (
        f"🦆 {found_word} DUCK\n\n"
        f"🔗 {link}"
    )

    await client.send_message(
        TARGET_CHANNEL,
        message
    )

    print("Отправлено:")
    print(message)
from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_ID, LOGGER_ID, CRIME_CHANNEL
from database.mongodb import warn_user, get_warns, reset_warns
import re

abusive_words = open("abusive_words/abusive.txt", "r").read().splitlines()

def warn_handlers(app):
    @app.on_message(filters.group & filters.text & ~filters.edited)
    async def detect_abuse(client, message: Message):
        if message.reply_to_message and message.from_user.id != OWNER_ID:
            text = message.reply_to_message.text or ""
        else:
            text = message.text or ""

        if any(re.search(rf"\b{re.escape(word)}\b", text.lower()) for word in abusive_words):
            try:
                await message.delete()
                await client.send_message(
                    CRIME_CHANNEL,
                    f"**Abuse Detected!**\n"
                    f"From: {message.from_user.mention} (`{message.from_user.id}`)\n"
                    f"Group: {message.chat.title}\n"
                    f"Link: [Jump to Message]({message.link})"
                )

                warns = await warn_user(message.chat.id, message.from_user.id)

                if warns >= 3:
                    await message.chat.restrict_member(
                        message.from_user.id,
                        permissions=None,
                        until_date=int((message.date + 86400).timestamp())
                    )
                    await message.reply_text(
                        f"{message.from_user.mention} muted for 24 hours due to 3 warnings!"
                    )
                    await reset_warns(message.chat.id, message.from_user.id)

            except Exception as e:
                print(f"Error in detect_abuse: {e}")

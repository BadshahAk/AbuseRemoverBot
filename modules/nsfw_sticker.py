from pyrogram import Client, filters
from pyrogram.types import Message
from config import CRIME_CHANNEL

@Client.on_message(filters.group & (filters.sticker | filters.animation))
async def sticker_check(client, message: Message):
    if "18+" in (message.sticker.set_name if message.sticker else ""):
        try:
            await message.delete()
            await client.send_message(
                CRIME_CHANNEL,
                f"**NSFW Sticker Detected!**\n"
                f"From: {message.from_user.mention}\n"
                f"Group: {message.chat.title}\n"
                f"Link: [Jump to Message]({message.link})"
            )
        except Exception as e:
            print(e)

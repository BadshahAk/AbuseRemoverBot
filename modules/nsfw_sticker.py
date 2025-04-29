from pyrogram import filters
from pyrogram.types import Message
from config import CRIME_CHANNEL

def nsfw_handlers(app):
    @app.on_message(filters.group & (filters.sticker | filters.animation))
    async def sticker_check(client, message: Message):
        try:
            sticker_set_name = ""

            if message.sticker:
                sticker_set_name = message.sticker.set_name or ""
            elif message.animation:
                sticker_set_name = message.animation.file_name or ""

            if "18+" in sticker_set_name.lower():
                await message.delete()
                await client.send_message(
                    CRIME_CHANNEL,
                    f"**NSFW Content Detected!**\n"
                    f"From: {message.from_user.mention} (`{message.from_user.id}`)\n"
                    f"Group: {message.chat.title}\n"
                    f"Link: [Jump to Message]({message.link})"
                )

        except Exception as e:
            print(f"Error in sticker_check: {e}")

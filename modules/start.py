from pyrogram import filters
from config import OWNER_ID, LOGGER_ID
from pyrogram.types import Message
from main import app  # Yeh zaroori hai!!

@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    await message.reply_text(
        f"**Hello {message.from_user.first_name}!**\n\n"
        "**I am AbuseRemoverBot!**\n"
        "Auto-removing abusive words and NSFW content!"
    )

    try:
        await client.send_message(
            LOGGER_ID,
            f"#NEW_USER\n\nName: {message.from_user.mention}\nUserID: `{message.from_user.id}`"
        )
    except Exception:
        pass

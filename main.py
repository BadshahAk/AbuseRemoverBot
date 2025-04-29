import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from modules.start import start_handler  # Decorator kaafi hai
from modules.warn import detect_abuse    # Decorator kaafi hai
from modules.nsfw_sticker import nsfw_handler  # Decorator kaafi hai
from pyrogram import idle

app = Client(
    "AbuseRemoverBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

print("Bot Started Successfully!")

async def main():
    await app.start()
    await idle()

if __name__ == "__main__":
    asyncio.run(main())

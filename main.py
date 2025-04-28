import asyncio
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from modules.start import start_handler  # Change to the actual function name
from modules.warn import warn_handlers
from modules.nsfw_sticker import nsfw_handlers

app = Client(
    "AbuseRemoverBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# No need to manually call start_handler here. Pyrogram handles this automatically via decorator.
warn_handlers(app)
nsfw_handlers(app)

print("Bot Started Successfully!")

async def main():
    await app.start()
    await idle()

if __name__ == "__main__":
    asyncio.run(main())

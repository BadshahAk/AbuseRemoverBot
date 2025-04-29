import asyncio
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from modules.warn import warn_handlers
from modules.nsfw_sticker import nsfw_handlers
import modules.start  # Required to auto-register start handler via decorator

app = Client(
    "AbuseRemoverBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Register all handlers
warn_handlers(app)
nsfw_handlers(app)

async def main():
    await app.start()
    print("Bot Started Successfully!")
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())

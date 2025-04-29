import asyncio
from pyrogram import Client
from pyrogram import idle
from config import API_ID, API_HASH, BOT_TOKEN
from modules.start import start_handler
from modules.warn import warn_handlers
from modules.nsfw_sticker import nsfw_handlers  # <-- Correct Import

app = Client(
    "AbuseRemoverBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Important: handlers ko app ke sath bind karna
warn_handlers(app)
nsfw_handlers(app)

print("Bot Started Successfully!")

async def main():
    await app.start()
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client["abuseremover"]
warnings = db["warnings"]

async def warn_user(chat_id, user_id):
    user = await warnings.find_one({"chat_id": chat_id, "user_id": user_id})
    if not user:
        await warnings.insert_one({"chat_id": chat_id, "user_id": user_id, "warns": 1})
        return 1
    else:
        warns = user["warns"] + 1
        await warnings.update_one(
            {"chat_id": chat_id, "user_id": user_id},
            {"$set": {"warns": warns}}
        )
        return warns

async def get_warns(chat_id, user_id):
    user = await warnings.find_one({"chat_id": chat_id, "user_id": user_id})
    return user["warns"] if user else 0

async def reset_warns(chat_id, user_id):
    await warnings.delete_one({"chat_id": chat_id, "user_id": user_id})

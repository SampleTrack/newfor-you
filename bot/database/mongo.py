from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import Config

client = AsyncIOMotorClient(Config.MONGO_URI)
db = client['auto_deals_bot']

users = db.users
channels = db.channels
deals = db.deals
posted = db.posted
settings = db.settings

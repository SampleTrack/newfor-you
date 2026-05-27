from pyrogram import Client
from bot.config import Config

bot = Client(
    'AutoDealsBot',
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    workers=50
)

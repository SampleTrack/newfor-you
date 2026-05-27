from pyrogram import filters
from pyrogram.types import Message
from bot.core.client import bot

@bot.on_message(filters.command('start'))
async def start_handler(client, message: Message):
    await message.reply_text(
        '🔥 Telegram Auto Deals Bot Running Successfully'
    )

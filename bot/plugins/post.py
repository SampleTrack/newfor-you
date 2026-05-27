from pyrogram import filters
from pyrogram.types import Message
from bot.core.client import bot
from bot.config import Config

@bot.on_message(filters.command('post') & filters.user(Config.OWNER_ID))
async def post_handler(client, message: Message):
    if len(message.command) < 3:
        return await message.reply_text('Usage: /post channel_id message')

    channel = message.command[1]
    text = ' '.join(message.command[2:])

    try:
        await bot.send_message(channel, text)
        await message.reply_text('✅ Posted Successfully')
    except Exception as e:
        await message.reply_text(str(e))

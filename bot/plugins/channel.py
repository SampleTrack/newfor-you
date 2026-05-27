from pyrogram import filters
from pyrogram.types import Message
from bot.core.client import bot
from bot.config import Config
from bot.database.mongo import channels

@bot.on_message(filters.command('addchannel') & filters.user(Config.OWNER_ID))
async def add_channel(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text('Usage: /addchannel channel_id')

    channel_id = message.command[1]

    exists = await channels.find_one({'channel_id': channel_id})
    if exists:
        return await message.reply_text('Channel already added')

    await channels.insert_one({'channel_id': channel_id})
    await message.reply_text('✅ Channel Added')

@bot.on_message(filters.command('channels') & filters.user(Config.OWNER_ID))
async def list_channels(client, message: Message):
    data = channels.find({})
    text = '📢 Channels:\n\n'

    async for channel in data:
        text += f"{channel['channel_id']}\n"

    await message.reply_text(text)

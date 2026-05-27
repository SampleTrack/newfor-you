from pyrogram import filters
from pyrogram.types import Message
from bot.core.client import bot
from bot.config import Config
from bot.core.queue import post_queue

@bot.on_message(filters.command('deal') & filters.user(Config.OWNER_ID))
async def add_deal(client, message: Message):
    if len(message.command) < 3:
        return await message.reply_text(
            'Usage: /deal link message'
        )

    link = message.command[1]
    text = ' '.join(message.command[2:])

    await post_queue.put({
        'link': link,
        'text': text
    })

    await message.reply_text('✅ Deal Added To Queue')

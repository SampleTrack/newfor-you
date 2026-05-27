from pyrogram import filters
from pyrogram.types import Message
from bot.core.client import bot
from bot.config import Config
from bot.core.queue import post_queue
from bot.utils.template import build_deal_post

@bot.on_message(filters.command('deal') & filters.user(Config.OWNER_ID))
async def add_deal(client, message: Message):
    if len(message.command) < 4:
        return await message.reply_text(
            'Usage: /deal title price link'
        )

    title = message.command[1]
    price = message.command[2]
    link = message.command[3]

    text = build_deal_post(title, price, link)

    await post_queue.put({
        'link': link,
        'text': text
    })

    await message.reply_text('✅ Deal Added To Queue')
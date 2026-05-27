from pyrogram import filters
from pyrogram.types import Message
from bot.core.client import bot
from bot.config import Config
from bot.core.queue import post_queue
from bot.utils.template import build_deal_post
import asyncio

@bot.on_message(filters.command('schedule') & filters.user(Config.OWNER_ID))
async def schedule_post(client, message: Message):
    if len(message.command) < 5:
        return await message.reply_text(
            'Usage: /schedule seconds title price link'
        )

    seconds = int(message.command[1])
    title = message.command[2]
    price = message.command[3]
    link = message.command[4]

    text = build_deal_post(title, price, link)

    async def delayed_post():
        await asyncio.sleep(seconds)

        await post_queue.put({
            'link': link,
            'text': text
        })

    asyncio.create_task(delayed_post())

    await message.reply_text('⏳ Deal Scheduled Successfully')

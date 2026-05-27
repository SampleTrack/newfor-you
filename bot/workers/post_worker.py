import asyncio
from pyrogram.errors import FloodWait
from bot.core.queue import post_queue
from bot.core.client import bot
from bot.database.mongo import channels
from bot.utils.duplicate import is_duplicate, save_post
from bot.utils.logger import logger

async def post_worker():
    while True:
        deal = await post_queue.get()

        try:
            link = deal.get('link')
            text = deal.get('text')

            if await is_duplicate(link):
                logger.info('Duplicate deal skipped')
                continue

            async for channel in channels.find({}):
                try:
                    await bot.send_message(
                        channel['channel_id'],
                        text,
                        disable_web_page_preview=False
                    )

                except FloodWait as e:
                    logger.warning(f'FloodWait: {e.value}')
                    await asyncio.sleep(e.value)

                except Exception as err:
                    logger.error(str(err))

            await save_post(link)

        except Exception as e:
            logger.error(str(e))

        post_queue.task_done()

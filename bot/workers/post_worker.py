import asyncio
from pyrogram.errors import FloodWait
from pyrogram.enums import ParseMode
from bot.core.client import bot
from bot.database.mongo import channels
from bot.utils.duplicate import is_duplicate, save_post
from bot.utils.logger import logger
from bot.utils.buttons import deal_button
from bot.database.queue_db import (
    get_pending_deals,
    mark_posted,
    mark_failed
)

async def post_worker():
    while True:
        deals = get_pending_deals()

        async for deal in deals:
            try:
                link = deal.get('link')
                text = deal.get('text')

                if await is_duplicate(link):
                    logger.info('Duplicate deal skipped')
                    await mark_posted(deal['_id'])
                    continue

                async for channel in channels.find({}):
                    try:
                        await bot.send_message(
                            channel['channel_id'],
                            text,
                            parse_mode=ParseMode.HTML,
                            reply_markup=deal_button(link),
                            disable_web_page_preview=False
                        )

                    except FloodWait as e:
                        logger.warning(f'FloodWait: {e.value}')
                        await asyncio.sleep(e.value)

                    except Exception as err:
                        logger.error(str(err))

                await save_post(link)
                await mark_posted(deal['_id'])

            except Exception as e:
                logger.error(str(e))
                await mark_failed(deal['_id'], str(e))

        await asyncio.sleep(10)

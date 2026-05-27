from fastapi import FastAPI
import asyncio
from bot.core.client import bot
import bot.core.loader
from bot.utils.logger import logger
from bot.workers.post_worker import post_worker

app = FastAPI()

@app.get('/')
async def health_check():
    return {'status': 'running'}

async def start_bot():
    await bot.start()
    logger.info('Bot Started Successfully')

    asyncio.create_task(post_worker())

    await asyncio.Event().wait()

@app.on_event('startup')
async def startup_event():
    asyncio.create_task(start_bot())

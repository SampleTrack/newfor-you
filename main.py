from fastapi import FastAPI
import asyncio
from bot.core.client import bot
import bot.core.loader
from bot.utils.logger import logger

app = FastAPI()

@app.get('/')
async def health_check():
    return {'status': 'running'}

async def start_bot():
    await bot.start()
    logger.info('Bot Started Successfully')
    await asyncio.Event().wait()

@app.on_event('startup')
async def startup_event():
    asyncio.create_task(start_bot())

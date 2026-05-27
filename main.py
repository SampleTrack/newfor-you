from fastapi import FastAPI
from pyrogram import Client
import asyncio
import os

app = FastAPI()

bot = Client(
    "auto-deals-bot",
    api_id=int(os.getenv("API_ID", 0)),
    api_hash=os.getenv("API_HASH", ""),
    bot_token=os.getenv("BOT_TOKEN", "")
)

@app.get("/")
async def health_check():
    return {"status": "running"}

async def start_bot():
    await bot.start()
    print("Bot Started")
    await asyncio.Event().wait()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_bot())

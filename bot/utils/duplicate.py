from bot.database.mongo import posted

async def is_duplicate(link: str):
    data = await posted.find_one({'link': link})
    return bool(data)

async def save_post(link: str):
    await posted.insert_one({'link': link})

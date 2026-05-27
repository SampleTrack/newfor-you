from bot.database.mongo import db
from datetime import datetime

queue_collection = db.queue

async def add_queue(data):
    data['status'] = 'pending'
    data['created_at'] = datetime.utcnow()
    data['retry_count'] = 0
    await queue_collection.insert_one(data)

async def get_pending_deals():
    return queue_collection.find({'status': 'pending'})

async def mark_posted(deal_id):
    await queue_collection.update_one(
        {'_id': deal_id},
        {'$set': {'status': 'posted'}}
    )

async def mark_failed(deal_id, error):
    await queue_collection.update_one(
        {'_id': deal_id},
        {
            '$set': {
                'status': 'failed',
                'last_error': str(error)
            },
            '$inc': {
                'retry_count': 1
            }
        }
    )

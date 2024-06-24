import asyncio
import json
from bot.commands import setup_bot
from web.routes import app
from database.models import init_db

def load_config():
    with open('config/config.json', 'r') as f:
        return json.load(f)

async def run_bot(config):
    bot = setup_bot(config)
    await bot.start(config['bot']['token'])

def run_web(config):
    app.run(host=config['web']['host'], port=config['web']['port'])

async def main():
    config = load_config()
    init_db(config['database']['url'])
    
    bot_task = asyncio.create_task(run_bot(config))
    web_task = asyncio.to_thread(run_web, config)
    
    await asyncio.gather(bot_task, web_task)

if __name__ == "__main__":
    asyncio.run(main())

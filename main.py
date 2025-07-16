import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers import start, ticker
from exchange.manager import ExchangeManager
from data.config import Config, load_config


config: Config = load_config()
bot = Bot(config.bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

exchange_manager = ExchangeManager()
ticker.exchange_manager = exchange_manager

dp.include_router(start.router)
dp.include_router(ticker.router)

async def main():
    await exchange_manager.initialize()
    try:
        await dp.start_polling(bot)
    finally:
        await exchange_manager.close()

if __name__ == "__main__":
    asyncio.run(main())
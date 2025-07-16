from aiogram import Router, F
from aiogram.types import Message
from utils.price_formatter import PriceFormatter


router = Router()
price_formatter = PriceFormatter
exchange_manager = None


@router.message(F.text & ~F.text.startswith("/") & (F.text.len() <= 5))
async def process_ticker(message: Message):
    ticker = message.text.upper().strip()

    prices = await exchange_manager.get_all_prices(ticker)

    if not exchange_manager.token_exists_anywhere(prices):
        await message.answer(f"no token '{ticker}' found")
        return

    formatted_message = price_formatter.format_prices(ticker, prices)

    await message.reply(formatted_message)

@router.message(F.text & ~F.text.startswith("/") & (F.text.len() > 5))
async def process_text_not_valid(message: Message):
    await message.answer(text="pls send me a ticker like BTC")

@router.message(~F.text)
async def process_non_text(message: Message):
    await message.answer(text="pls send me a ticker like BTC")
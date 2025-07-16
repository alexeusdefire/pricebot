from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
router = Router()

@router.message(CommandStart())
async def process_start(message: Message):
    await message.answer(text="type token ticker to see current price on Binance, "
                              "ByBit, MEXC, GateIo, BingX")

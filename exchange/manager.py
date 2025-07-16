import asyncio
from .binance import BinanceExchange
from .bybit import BybitExchange
from .mexc import MexcExchange
from .gate import GateExchange
from .bingx import BingxExchange
from .okx import OKXExchange

class ExchangeManager:
    def __init__(self):
        self.exchanges = [
            BinanceExchange(),
            BybitExchange(),
            MexcExchange(),
            GateExchange(),
            BingxExchange(),
            OKXExchange()
        ]

    async def initialize(self):
        for exchange in self.exchanges:
            await exchange.create_session()

    async def close(self):
        for exchange in self.exchanges:
            await exchange.close_session()

    async def get_all_prices(self, ticker):
        tasks = []
        for exchange in self.exchanges:
            tasks.append(exchange.get_price(ticker))

        results = await asyncio.gather(*tasks)

        prices = {}
        for i, exchange in enumerate(self.exchanges):
            prices[exchange.name] = results[i]

        return prices

    def token_exists_anywhere(self, prices):
        for price in prices.values():
            if price != "no token":
                return True
        return False
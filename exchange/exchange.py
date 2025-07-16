import aiohttp


class BaseExchange:
    def __init__(self, base_url, name):
        self.base_url = base_url
        self.name = name
        self.session = None

    async def create_session(self):
        self.session = aiohttp.ClientSession()

    async def close_session(self):
        if self.session:
            await self.session.close()

    def format_ticker(self, ticker):
        return f"{ticker.upper()}USDT"
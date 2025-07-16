from .exchange import BaseExchange


class BinanceExchange(BaseExchange):
    def __init__(self):
        super().__init__(
            base_url="https://api.binance.com/api/v3",
            name="Binance"
        )

    def format_ticker(self, ticker):
        return f"{ticker.upper()}USDT"

    async def get_price(self, ticker):
        try:
            formatted_ticker = self.format_ticker(ticker)
            url = f"{self.base_url}/ticker/price?symbol={formatted_ticker}"

            async with self.session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['price']
                else:
                    return "no token"
        except:
            return "no token"
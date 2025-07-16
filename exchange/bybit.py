from .exchange import BaseExchange


class BybitExchange(BaseExchange):
    def __init__(self):
        super().__init__(
            base_url="https://api.bybit.com/v5/market",
            name="Bybit"
        )

    def format_ticker(self, ticker):
        return f"{ticker.upper()}USDT"

    async def get_price(self, ticker):
        try:
            formatted_ticker = self.format_ticker(ticker)
            url = f"{self.base_url}/tickers?category=spot&symbol={formatted_ticker}"

            async with self.session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    if data['retCode'] == 0:
                        return data["result"]["list"][0]["lastPrice"]
                    else:
                        return "no token"
                else:
                    return "no token"
        except:
            return "no token"
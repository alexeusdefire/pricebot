from .exchange import BaseExchange


class OKXExchange(BaseExchange):
    def __init__(self):
        super().__init__(
            base_url="https://www.okx.com/api/v5/market",
            name="OKX"
        )

    def format_ticker(self, ticker):
        return f"{ticker.upper()}-USDT"

    async def get_price(self, ticker):
        try:
            formatted_ticker = self.format_ticker(ticker)
            url = f"{self.base_url}/ticker?instId={formatted_ticker}"

            async with self.session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    if data["code"] == 0:
                        return data["data"][0]["last"]
                    else:
                        return "no token"
                else:
                    return "no token"
        except:
            return "no token"
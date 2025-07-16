from .exchange import BaseExchange


class GateExchange(BaseExchange):
    def __init__(self):
        super().__init__(
            base_url="https://api.gateio.ws/api/v4",
            name="Gate.io"
        )

    def format_ticker(self, ticker):
        return f"{ticker.upper()}_USDT"

    async def get_price(self, ticker):
        try:
            formatted_ticker = self.format_ticker(ticker)
            url = f"{self.base_url}/spot/tickers?currency_pair={formatted_ticker}"

            async with self.session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    if data:
                        return data[0]['last']
                    else:
                        return "no token"
                else:
                    return "no token"
        except:
            return "no token"
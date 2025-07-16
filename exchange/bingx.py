from .exchange import BaseExchange


class BingxExchange(BaseExchange):
    def __init__(self):
        super().__init__(
            base_url="https://open-api.bingx.com/openApi/spot/v1",
            name="BingX"
        )

    def format_ticker(self, ticker):
        return f"{ticker.upper()}-USDT"

    async def get_price(self, ticker):
        try:
            formatted_ticker = self.format_ticker(ticker)
            url = f"{self.base_url}/ticker/price?symbol={formatted_ticker}"

            async with self.session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    if data['code'] == 0:
                        return data['data'][0]["trades"][0]['price']
                    else:
                        return "no token"
                else:
                    return "no token"
        except:
            return "no token"
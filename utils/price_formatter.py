class PriceFormatter:
    @staticmethod
    def format_prices(ticker, prices):
        if not PriceFormatter.token_exists_anywhere(prices):
            return f"No token '{ticker}' found"

        message = f"<code>{ticker.upper()} prices\n\n"

        for exchange_name, price in prices.items():
            if price == "no token":
                message += f"{exchange_name}: no token\n"
            else:
                message += f"{exchange_name}: ${price}\n"

        message += "</code>"

        return message

    @staticmethod
    def token_exists_anywhere(prices):
        for price in prices.values():
            if price != "no token":
                return True
        return False
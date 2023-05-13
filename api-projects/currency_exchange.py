# currency_converter.py

class CurrencyConverter:
    # hard-coded values for INR to USD and USD to INR conversion
    exchange_rates = {
        "INR_USD": 0.014,
        "USD_INR": 71.17,
    }

    @staticmethod
    def convert(from_currency: str, to_currency: str, value: float) -> tuple[float, float]:
        """Converts a value from one currency to another and returns the converted value and exchange rate"""
        exchange_rate_key = f"{from_currency.upper()}_{to_currency.upper()}"
        if exchange_rate_key not in CurrencyConverter.exchange_rates:
            raise ValueError(f"Unsupported currency pair: {from_currency}-{to_currency}")
        exchange_rate = CurrencyConverter.exchange_rates[exchange_rate_key]
        converted_value = exchange_rate * value
        return converted_value, exchange_rate

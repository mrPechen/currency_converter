import pandas as pd
from api.cache import Cache
from fastapi.responses import JSONResponse


class Converter:
    def __init__(self):
        self.file = 'https://www.cbr-xml-daily.ru/daily_json.js'
        self.cache = Cache()

    def read_data(self):
        cache = self.cache.get_cache()
        if cache:
            cache_df = pd.DataFrame(pd.read_json(cache))
            return cache_df
        df = pd.DataFrame(pd.read_json(self.file))
        data = df.to_json()
        self.cache.set_cache(data)
        return df

    def get_currency_value(self, currency: str):
        data = self.read_data()
        currency_value = float
        if currency == 'RUB':
            return 1
        for i in data.iterrows():
            if i[1]['Valute']['CharCode'] == currency:
                if i[1]['Valute']['Nominal'] > 1:
                    currency_value = i[1]['Valute']['Value'] / i[1]['Valute']['Nominal']
                else:
                    currency_value = i[1]['Valute']['Value']
        return currency_value

    def counting(self, from_currency: str, to_currency: str, value: int | float):
        try:
            from_currency_value = self.get_currency_value(from_currency)
            to_currency_value = self.get_currency_value(to_currency)
            result = format(from_currency_value / to_currency_value * value, '.2f')
            return JSONResponse({"result": f"{result}"})
        except TypeError:
            return JSONResponse({"error": f"one of currencies not found"})

    def converter(self, from_currency: str, to_currency: str, value: int | float):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        return self.counting(from_currency=from_currency, to_currency=to_currency, value=value)

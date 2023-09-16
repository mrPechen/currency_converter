from fastapi import FastAPI
from api.converter_service import Converter


app = FastAPI()


@app.get('/api/rates')
def run_converter(from_cur: str | None = None, to: str | None = None, value: int | float | None = None):
    return Converter().converter(from_currency=from_cur, to_currency=to, value=value)

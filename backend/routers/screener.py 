from fastapi import APIRouter

router = APIRouter()

@router.get("/bullish")
def get_bullish_stocks(tickers: str):
    return {"tickers": tickers.split(","), "message": "Bullish screener working"}
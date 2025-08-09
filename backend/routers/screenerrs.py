from fastapi import APIRouter

router = APIRouter()

@router.get("/bullish")
async def get_bullish_stocks(tickers: str):
    # your screener logic here
    return {"tickers": tickers.split(",")}

from fastapi import APIRouter

router = APIRouter()

@router.get("/bullish")
def get_bullish(tickers: str):
    tickers_list = tickers.split(",")
    # Placeholder logic (replace with Alpaca/Plaid logic later)
    return {"requested_tickers": tickers_list, "status": "success"}

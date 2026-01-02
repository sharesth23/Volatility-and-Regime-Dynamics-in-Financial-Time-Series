import yfinance as yf
import pandas as pd

def load_sp500(start="2000-01-01"):
    df = yf.download("^GSPC", start=start, progress=False)

    prices = df["Adj Close"].dropna()
    returns = prices.pct_change().dropna()

    return prices, returns

from datetime import datetime
import pandas as pd
import yfinance as yf
from config import STOCKS, START_DATE, END_DATE

def fetch_stock_data():
    all_dfs = []
    for symbol, ticker in STOCKS.items():
        print(f"Fetching data for {symbol}...")
        df = yf.download(
            ticker,
            start=START_DATE,
            end=END_DATE,
            progress=False,
            auto_adjust=False
        )
        if df.empty:
            print(f"No data found for {symbol}")
            continue
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        df = df.reset_index()
        result = pd.DataFrame({
            "stock_symbol": symbol,
            "trade_date": pd.to_datetime(df["Date"]).dt.date,
            "closing_price": df["Close"].round(2),
            "volume": df["Volume"].astype("int64"),
            "load_timestamp":  datetime.now()
        })
        all_dfs.append(result)

    if not all_dfs:
        return pd.DataFrame()
    return pd.concat(all_dfs, ignore_index=True)
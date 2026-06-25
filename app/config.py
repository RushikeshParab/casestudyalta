from datetime import datetime, timedelta
STOCKS = {
    "RELIANCE": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "INFY": "INFY.NS"
}
yesterday = datetime.now() - timedelta(days=1)
START_DATE = yesterday.strftime("%Y-%m-%d")
END_DATE = (yesterday + timedelta(days=1)).strftime("%Y-%m-%d")
OUTPUT_FILE = "output/daily_prices.csv"
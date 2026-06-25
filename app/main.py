

from bigquery_loader import load_to_bigquery
from fetch_stock import fetch_stock_data


def main():
    df = fetch_stock_data()

    if df.empty:
        print("\nNo stock data found.")
        return

    print("\nFetched Data:\n")
    load_to_bigquery(df)

    print("\nPipeline completed successfully.")
    print(f"Exported {len(df)} rows.")


if __name__ == "__main__":
    main()
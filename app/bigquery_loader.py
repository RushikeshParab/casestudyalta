from google.cloud import bigquery

PROJECT_ID = "Project_ID-False"
DATASET = "stock_data"
TABLE = "daily_prices"

def load_to_bigquery(df):

    client = bigquery.Client(project=PROJECT_ID)

    table_id = f"{PROJECT_ID}.{DATASET}.{TABLE}"

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )

    job = client.load_table_from_dataframe(
        df,
        table_id,
        job_config=job_config
    )

    job.result()

    print(f"Loaded {len(df)} rows into {table_id}")
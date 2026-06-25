resource "google_bigquery_dataset" "stock_data" {
  dataset_id = "stock_data"
  location   = "asia-south1"
}

resource "google_bigquery_table" "daily_prices" {

  dataset_id = google_bigquery_dataset.stock_data.dataset_id
  table_id   = "daily_prices"

  deletion_protection = false

  schema = file("${path.module}/schema.json")
}

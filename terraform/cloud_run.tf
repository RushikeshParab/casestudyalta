resource "google_cloud_run_v2_job" "stock_pipeline" {

  name     = "stock-data-pipeline"
  location = var.region
  template {
    template {
      service_account = google_service_account.cloud_run_sa.email
      containers {
        image = "asia-south1-docker.pkg.dev/${var.project_id}/stock-pipeline/stock-data-pipeline:v2"
      }
      max_retries = 1
      timeout = "600s"

    }
  }

  deletion_protection = false
}
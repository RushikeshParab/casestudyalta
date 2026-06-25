resource "google_service_account" "cloud_run_sa" {
  account_id   = ""
  display_name = "Stock Pipeline Service Account"
}

resource "google_project_iam_member" "bigquery_editor" {
  project = var.project_id
  role = "roles/bigquery.jobUser"
  member = "serviceAccount:${google_service_account.cloud_run_sa.email}"
}

resource "google_project_iam_member" "bigquery_data_editor" {
  project = var.project_id

  role   = "roles/bigquery.dataEditor"
  member = "serviceAccount:${google_service_account.cloud_run_sa.email}"
}
resource "google_artifact_registry_repository" "stock_repo" {

  location      = var.region
  repository_id = "stock-pipeline"

  description = "Docker repository for stock pipeline"

  format = "DOCKER"
}
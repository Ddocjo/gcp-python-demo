resource "google_artifact_registry_repository" "repo" {
  location      = var.region
  repository_id = var.artifact_repo_name
  description   = "Docker repo for GCP python demo"
  format        = "DOCKER"
}

resource "google_service_account" "run_sa" {
  account_id   = "cloudrun-runtime-sa"
  display_name = "Cloud Run Runtime Service Account"
}

resource "google_secret_manager_secret" "app_secret" {
  secret_id = var.secret_name

  replication {
    auto {}
  }
}

resource "google_secret_manager_secret_iam_member" "run_sa_secret_access" {
  secret_id = google_secret_manager_secret.app_secret.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.run_sa.email}"
}
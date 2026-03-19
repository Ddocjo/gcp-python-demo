output "artifact_repo" {
  value = google_artifact_registry_repository.repo.repository_id
}

output "artifact_repo_location" {
  value = google_artifact_registry_repository.repo.location
}

output "runtime_service_account_email" {
  value = google_service_account.run_sa.email
}

output "secret_name" {
  value = google_secret_manager_secret.app_secret.secret_id
}
variable "project_id" {
  type = string
    default = "gcp-python-demo-489721"
}

variable "region" {
  type    = string
  default = "europe-west1"
}

variable "artifact_repo_name" {
  type    = string
  default = "gcp-python-demo"
}

variable "service_name" {
  type    = string
  default = "gcp-python-demo"
}

variable "secret_name" {
  type    = string
  default = "demo-api-key"
}
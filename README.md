# GCP Python CI/CD Security Demo

A lightweight end to end Google Cloud demo showing how to build, test, scan, store, and deploy a Python service securely using Docker, Artifact Registry, Cloud Run, Secret Manager, Terraform, and Cloud Build.

This project was built to demonstrate practical cloud engineering, security, and CI/CD concepts in a small but complete deployment flow.

---

## Project objectives

This project was designed to demonstrate how to:

- containerize a Python FastAPI application with Docker
- store container images in Artifact Registry
- deploy a service to Cloud Run
- keep the Cloud Run service private with authenticated invocation only
- use a dedicated runtime service account
- retrieve secrets from Secret Manager at runtime
- provision supporting infrastructure with Terraform
- automate validation, testing, image build, push, and deployment with Cloud Build
- emit structured logs for operational visibility
- enable vulnerability scanning on container images

---

## Solution overview

The final solution consists of:

- a small FastAPI application with health, hello, and secret validation endpoints
- a Docker image built from the application
- an Artifact Registry repository for image storage
- a private Cloud Run service for serverless execution
- a Secret Manager secret accessed at runtime
- a dedicated Cloud Run runtime service account
- Terraform-managed supporting infrastructure
- a Cloud Build CI/CD pipeline
- structured application logs in Cloud Logging
- Artifact Registry vulnerability scanning

---

## Architecture

### High level flow

1. Code is stored in GitHub
2. A push triggers Cloud Build
3. Cloud Build validates deployment configuration
4. Cloud Build runs tests
5. Cloud Build builds the Docker image
6. Cloud Build pushes the image to Artifact Registry
7. Cloud Build deploys the image to Cloud Run
8. Cloud Run runs the service with a dedicated runtime service account
9. The application retrieves a secret from Secret Manager at runtime
10. Runtime and pipeline logs are written to Cloud Logging

---

## Technology stack

- **Language:** Python 3.11
- **Framework:** FastAPI
- **Containerization:** Docker
- **Infrastructure as Code:** Terraform
- **CI/CD:** Cloud Build
- **Container Registry:** Artifact Registry
- **Runtime:** Cloud Run
- **Secrets:** Secret Manager
- **Logging:** Cloud Logging
- **Source Control:** GitHub

---

## Repository structure

```text
gcp-python-demo/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ tests/
│  └─ test_health.py
├─ scripts/
│  └─ validate_config.py
├─ infra/
│  ├─ main.tf
│  ├─ provider.tf
│  ├─ variables.tf
│  ├─ outputs.tf
│  ├─ terraform.tfvars
│  └─ versions.tf
├─ cloudbuild.yaml
├─ .gitignore
└─ README.md
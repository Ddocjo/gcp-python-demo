## Security controls
- Private Cloud Run service with authenticated invocation only
- Dedicated runtime service account
- Secret stored in Secret Manager
- Artifact Registry image storage and vulnerability scanning
- CI validation gate to block insecure deployment config

## Observability
- Structured JSON logs
- Cloud Run metrics in Cloud Monitoring
- Alert policy for reliability/performance issues
- OpenTelemetry-based trace export to Cloud Trace

## CI/CD
- GitHub push trigger
- Automated tests
- Container build and push
- Automated deploy to Cloud Run
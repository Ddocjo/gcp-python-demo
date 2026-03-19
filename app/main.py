import json
import logging
import os

from fastapi import FastAPI
from google.cloud import secretmanager

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")


def get_secret(secret_id: str, project_id: str) -> str:
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")


@app.get("/health")
def health():
    logger.info(json.dumps({
        "event": "health_check",
        "status": "ok"
    }))
    return {"status": "ok"}


@app.get("/hello")
def hello():
    logger.info(json.dumps({
        "event": "hello_called"
    }))
    return {"message": "Hello from GCP python demo"}


@app.get("/secret-check")
def secret_check():
    project_id = os.getenv("GCP_PROJECT")
    secret_id = os.getenv("APP_SECRET_ID", "demo-api-key")

    if not project_id:
        return {"ok": False, "error": "GCP_PROJECT env var not set"}

    value = get_secret(secret_id, project_id)

    logger.info(json.dumps({
        "event": "secret_access_success",
        "secret_id": secret_id
    }))

    return {
        "ok": True,
        "secret_id": secret_id,
        "secret_length": len(value)
    }
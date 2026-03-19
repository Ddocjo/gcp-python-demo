import os
import sys

required_env_vars = [
    "PROJECT_ID",
    "REGION",
    "SERVICE_NAME",
    "SERVICE_ACCOUNT",
    "SECRET_NAME",
    "REPO_NAME",
]

missing = [v for v in required_env_vars if not os.getenv(v)]

if missing:
    print(f"Missing required environment variables: {', '.join(missing)}")
    sys.exit(1)

if os.getenv("ALLOW_UNAUTHENTICATED", "false").lower() == "true":
    print("Unauthenticated deployment is not allowed for this project.")
    sys.exit(1)

print("Config validation passed.")
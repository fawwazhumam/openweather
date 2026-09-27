#!/usr/bin/env bash
# Runs on the VPS (piped over SSH by .github/workflows/deploy.yml).
# Usage: deploy.sh <deploy_path> <git_sha> <airflow_port>
set -euo pipefail

DEPLOY_PATH="$1"
SHA="$2"
AIRFLOW_PORT="$3"

cd "$DEPLOY_PATH"

echo "Deploying $SHA to $DEPLOY_PATH"
git fetch --quiet origin
git reset --hard "$SHA"

docker compose pull --quiet
docker compose up -d --remove-orphans

echo "Waiting for Airflow to become healthy..."
for _ in $(seq 1 30); do
  if curl -fsS "http://127.0.0.1:${AIRFLOW_PORT}/api/v2/monitor/health" > /dev/null; then
    echo "Airflow is healthy"
    exit 0
  fi
  sleep 10
done

echo "Airflow did not become healthy in time"
docker compose ps
docker compose logs --tail 50 airflow
exit 1

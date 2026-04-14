#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_DIR="$ROOT/.conda-recovered"
REQ_FILE="$ROOT/assembled/requirements-local.txt"
TMP_REQ="$(mktemp)"

cleanup() {
  rm -f "$TMP_REQ"
}
trap cleanup EXIT

if ! command -v conda >/dev/null 2>&1; then
  echo "conda not found in PATH" >&2
  exit 1
fi

grep -v '^PySide6==' "$REQ_FILE" > "$TMP_REQ"

conda create -y -p "$ENV_DIR" -c conda-forge python=3.11 pip pyside6
"$ENV_DIR/bin/python" -m pip install -r "$TMP_REQ"

mkdir -p "$ROOT/.cache/matplotlib-conda"

cat <<EOF
Conda environment created at:
  $ENV_DIR

Run the recovered apps with:
  $ROOT/tools/run_recovered_app.sh mondo
  $ROOT/tools/run_recovered_app.sh acheron
EOF

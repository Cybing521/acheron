#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_DIR="$ROOT/.conda-recovered"
REQ_FILE="$ROOT/assembled/requirements-local.txt"

if ! command -v conda >/dev/null 2>&1; then
  echo "conda not found in PATH" >&2
  exit 1
fi

if [[ ! -x "$ENV_DIR/bin/python" ]]; then
  conda create -y -p "$ENV_DIR" -c conda-forge python=3.11 pip
fi

conda install -y -p "$ENV_DIR" -c conda-forge python.app
"$ENV_DIR/bin/python" -m pip install -r "$REQ_FILE"

mkdir -p "$ROOT/.cache/matplotlib-conda"

cat <<EOF
Conda environment created at:
  $ENV_DIR

Run the recovered apps with:
  $ROOT/tools/run_recovered_app.sh mondo
  $ROOT/tools/run_recovered_app.sh acheron
EOF

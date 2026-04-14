#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="$ROOT/.conda-recovered/bin/python"
BOOTSTRAP="$ROOT/tools/bootstrap_recovered_app.py"

if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "Missing conda environment at $ROOT/.conda-recovered" >&2
  echo "Run: $ROOT/tools/setup_conda_env.sh" >&2
  exit 1
fi

mkdir -p "$ROOT/.cache/matplotlib-conda"
export MPLCONFIGDIR="$ROOT/.cache/matplotlib-conda"

exec "$PYTHON_BIN" "$BOOTSTRAP" "$@"

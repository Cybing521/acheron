#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_DIR="$ROOT/.conda-recovered"
REQ_FILE="$ROOT/assembled/requirements-local.txt"
SITE_PACKAGES="$ENV_DIR/lib/python3.11/site-packages"
LOCAL_PYSIDE_SITE="$HOME/Library/Python/3.9/lib/python/site-packages"
LOCAL_PYSIDE_VERSION=""

if ! command -v conda >/dev/null 2>&1; then
  echo "conda not found in PATH" >&2
  exit 1
fi

if [[ ! -x "$ENV_DIR/bin/python" ]]; then
  conda create -y -p "$ENV_DIR" -c conda-forge python=3.11 pip
fi

conda install -y -p "$ENV_DIR" -c conda-forge python.app

if [[ -d "$LOCAL_PYSIDE_SITE/PySide6" && -d "$LOCAL_PYSIDE_SITE/shiboken6" ]]; then
  LOCAL_PYSIDE_VERSION="$(
    PYTHONPATH="$LOCAL_PYSIDE_SITE" python3 - <<'PY'
import PySide6
print(PySide6.__version__)
PY
  )"
fi

if [[ "$LOCAL_PYSIDE_VERSION" == "6.10.3" ]]; then
  rm -rf \
    "$SITE_PACKAGES"/PySide6 \
    "$SITE_PACKAGES"/shiboken6 \
    "$SITE_PACKAGES"/PySide6-*.dist-info \
    "$SITE_PACKAGES"/PySide6_Addons-*.dist-info \
    "$SITE_PACKAGES"/PySide6_Essentials-*.dist-info \
    "$SITE_PACKAGES"/shiboken6-*.dist-info
  mkdir -p "$SITE_PACKAGES"
  rsync -a "$LOCAL_PYSIDE_SITE/PySide6/" "$SITE_PACKAGES/PySide6/"
  rsync -a "$LOCAL_PYSIDE_SITE/shiboken6/" "$SITE_PACKAGES/shiboken6/"
  if [[ -d "$LOCAL_PYSIDE_SITE/shiboken6-6.10.3.dist-info" ]]; then
    rsync -a "$LOCAL_PYSIDE_SITE/shiboken6-6.10.3.dist-info/" "$SITE_PACKAGES/shiboken6-6.10.3.dist-info/"
  fi
  grep -v '^PySide6==' "$REQ_FILE" > "$ENV_DIR/.requirements-no-pyside6.txt"
  "$ENV_DIR/bin/python" -m pip install --upgrade -r "$ENV_DIR/.requirements-no-pyside6.txt"
else
  "$ENV_DIR/bin/python" -m pip install --upgrade -r "$REQ_FILE"
fi

mkdir -p "$ROOT/.cache/matplotlib-conda"

cat <<EOF
Conda environment created at:
  $ENV_DIR

Run the recovered apps with:
  $ROOT/tools/run_recovered_app.sh mondo
  $ROOT/tools/run_recovered_app.sh acheron
EOF

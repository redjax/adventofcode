#!/bin/bash

if ! command -v uv &> /dev/null; then
  echo "Error: uv command not found. Please install uv and try again: https://docs.astral.sh/uv"
  exit 1
fi

JUPYTER_TOKEN=${JUPYTER_TOKEN:-""}
JUPYTER_PASSWORD=${JUPYTER_PASSWORD:-""}

JUPYTER_ROOT=$(pwd)/.jupyter
JUPYTER_CONFIG_ROOT="${JUPYTER_ROOT}/config"

export JUPYTER_CONFIG_DIR="${JUPYTER_CONFIG_ROOT}"
export JUPYTER_CONFIG_PATH="${JUPYTER_CONFIG_DIR}"
export JUPYTERLAB_DIR="${JUPYTER_ROOT}/lab"
export JUPYTERLAB_SETTINGS_DIR="${JUPYTERLAB_DIR}"
export JUPYTER_RUNTIME_DIR="${JUPYTER_ROOT}/runtime"
export JUPYTER_DATA_DIR="${JUPYTER_ROOT}/data"

if [ ! -d "${JUPYTERLAB_DIR}" ]; then
    echo "[WARNING] Jupyter lab directory not found, creating path: ${JUPYTERLAB_DIR}"
    uv run jupyter lab build

    if [ ! $? -eq 0 ]; then
        echo "[ERROR] Jupyter lab build failed"
        exit 1
    fi
fi

## Uncomment for debugging
# uv run jupyter --config-dir
# uv run jupyter --paths
# uv run jupyter lab path

echo "Installing project"

uv build
uv sync --dev
uv pip install .

echo "Starting Jupyter lab"

uv run jupyter lab --config="${JUPYTER_CONFIG_DIR}/jupyter_lab_config.py" "$@" --IdentityProvider.token=$JUPYTER_TOKEN --ServerApp.default_url="/lab?file-browser-path=/years"

#!/bin/bash

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

echo "Starting Jupyter lab"

uv run jupyter lab --config="${JUPYTER_CONFIG_DIR}/jupyter_lab_config.py" "$@" --ServerApp.token=''

# uv run jupyter --config-dir
# uv run jupyter --paths
uv run jupyter lab path

#!/bin/bash

export JUPYTER_CONFIG_DIR=$(pwd)/.jupyter/jupyter_config
export JUPYTER_CONFIG_PATH=$JUPYTER_CONFIG_DIR
export JUPYTER_RUNTIME_DIR=$(pwd)/.jupyter/jupyter_runtime
export JUPYTER_DATA_DIR=$(pwd)/.jupyter/jupyter_data

echo "Starting Jupyter lab"

uv run jupyter lab --config="${JUPYTER_CONFIG_DIR}/jupyter_lab_config.py" "$@" --LabApp.token=''
# uv run jupyter --config-dir

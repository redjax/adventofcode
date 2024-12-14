# Advent of Code

My solutions for [Advent of Code](https://adventofcode.com). Most solutions are in Python, and may include a Jupyter notebook.

## Requirements

- [uv](https://docs.astral.sh/uv)
- (Optional) [Python](https://python.org)
  - `uv` can handle installing Python for you. Run command with `uv --python` to use the `uv`-managed Python interpreter.

## Usage

As of 12/14/24, this repository uses Jupyter Lab and Jupyter notebooks for solutions. You can start a Jupyter Lab environment in one of 2 ways; first, you can simply run the [`run_jupyter_lab.sh`](./scripts/run_jupyter_lab.sh) script, which sets Jupyter environment variables for the current session and launches it.

Second, you can declare each of the environment variables below (`export $VarName=Value` on Linux/Mac, `${env:VarName}=Value` on Windows), then run `uv run jupyter lab --config="${JUPYTER_CONFIG_DIR}/jupyter_lab_config.py" "$@" --IdentityProvider.token=$JUPYTER_TOKEN`.

| variable name | default/suggested value | purpose |
| ------------- | ----------------------- | ------- |
| `JUPYTER_TOKEN` | `""` | Enable or disable a token you must enter to open the web UI. |
| `JUPYTER_PASSWORD` | `""` | Enable or disable a password you must enter to open the web UI. |
| `JUPYTER_ROOT` | `$(pwd)/.jupyter` | Working directory for Jupyter/Lab. |
| `JUPYTER_CONFIG_ROOT` | `$(pwd)/.jupyter/config` | Path to Jupyter configurations. |
| `JUPYTER_CONFIG_DIR` | `$(pwd)/.jupyter` | (same as config root variable) Tells Jupyter where to look for configurations. |
| `JUPYTER_CONFIG_PATH` | `$(pwd)/.jupyter` | (same as config root variable) Both `JUPYTER_CONFIG_{DIR,PATH}` seem to be required... |
| `JUPYTERLAB_DIR` | `$(pwd)/.jupyter/lab` | Working directory for Jupyter Lab. |
| `JUPYTERLAB_SETTINGS_DIR` | `$(pwd)/.jupyter/lab` | Path where Jupyter Lab should look for configurations. |
| `JUPYTER_RUNTIME_DIR` | `$(pwd)/.jupyter/runtime` | Path where Jupyter will store its runtime environment (binaries, generated files, etc). |
| `JUPYTER_DATA_DIR` | `$(pwd)/.jupyter/data` | Path where Jupyter will store data like the `file_id_manager.db`. |

Instead of exporting/setting these variables, you can also prepend the `uv run jupyter lab` command with your variables, like:

```shell
## Export Jupyter env vars and run lab command
export JUPYTER_TOKEN="" \
export JUPYTER_PASSWORD="" \
export JUPYTER_ROOT=$(pwd)/.jupyter \
export JUPYTER_CONFIG_ROOT=$(pwd)/.jupyter/config \
export JUPYTER_CONFIG_DIR=$(pwd)/.jupyter \
export JUPYTER_CONFIG_PATH=$(pwd)/.jupyter \
export JUPYTERLAB_DIR=$(pwd)/.jupyter/lab \
export JUPYTERLAB_SETTINGS_DIR=$(pwd)/.jupyter/lab \
export JUPYTER_RUNTIME_DIR=$(pwd)/.jupyter/runtime \
export JUPYTER_DATA_DIR=$(pwd)/.jupyter/data \
uv run jupyter lab --config="${JUPYTER_CONFIG_DIR}/jupyter_lab_config.py" "$@" --ServerApp.token=$JUPYTER_TOKEN
```

### Change starting path

You can set the path Jupyter Lab opens in the web UI using `--ServerApp.default_url='/lab?file-browser-path=/path/to/open'`
--ServerApp.default_url="/lab?file-browser-path=/years"

## Years

- [2024](./years/2024/)

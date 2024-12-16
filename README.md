# Advent of Code <!-- omit in toc -->

My solutions for [Advent of Code](https://adventofcode.com). Most solutions are in Python, and may include a Jupyter notebook.

# Table of Contents <!-- omit in toc -->
- [Requirements](#requirements)
- [Years](#years)
- [Usage](#usage)
  - [Method 1: Using the `uv` project manager](#method-1-using-the-uv-project-manager)
  - [Method 2: Use environment variables \& run manually](#method-2-use-environment-variables--run-manually)
- [Automatic port binding](#automatic-port-binding)
- [Change Jupyter Lab's starting path](#change-jupyter-labs-starting-path)

## Requirements

- [uv](https://docs.astral.sh/uv)
- (Optional) [Python](https://python.org)
  - `uv` can handle installing Python for you. Run command with `uv --python` to use the `uv`-managed Python interpreter.

## Years

Click on a year below to see code/solutions for that year.

- [2024](./years/2024/)

## Usage

As of 12/14/24, this repository uses Jupyter Lab and Jupyter notebooks for solutions. You can start a Jupyter Lab environment in one of 2 ways.

### Method 1: Using the `uv` project manager

If you are on Linux or Mac, you can simply run the [`run_jupyter_lab.sh`](./scripts/run_jupyter_lab.sh) script, which sets Jupyter environment variables for the current session and launches it.

When your Jupyter Lab environment is running, it will be accessible at `http://{server-ip}:8000` by default. If port `8000` is in use, the app will iterate over ports starting at `8000` using the `socket` Python library, and will bind to the first free/open port.

### Method 2: Use environment variables & run manually

You can declare each of the environment variables below (`export $VarName=Value` on Linux/Mac, `${env:VarName}=Value` on Windows), then run `uv run jupyter lab --config="${JUPYTER_CONFIG_DIR}/jupyter_lab_config.py" "$@" --IdentityProvider.token=$JUPYTER_TOKEN`.

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
JUPYTER_TOKEN="" \
JUPYTER_PASSWORD="" \
JUPYTER_ROOT=$(pwd)/.jupyter \
JUPYTER_CONFIG_ROOT=$(pwd)/.jupyter/config \
JUPYTER_CONFIG_DIR=$(pwd)/.jupyter \
JUPYTER_CONFIG_PATH=$(pwd)/.jupyter \
JUPYTERLAB_DIR=$(pwd)/.jupyter/lab \
JUPYTERLAB_SETTINGS_DIR=$(pwd)/.jupyter/lab \
JUPYTER_RUNTIME_DIR=$(pwd)/.jupyter/runtime \
JUPYTER_DATA_DIR=$(pwd)/.jupyter/data \
uv run jupyter lab --config="${JUPYTER_CONFIG_DIR}/jupyter_lab_config.py" "$@" --ServerApp.token=$JUPYTER_TOKEN
```

## Automatic port binding

The [Jupyter Lab configuration file](./.jupyter/config/jupyter_lab_config.py) uses the `find_free_port()` function shown below to bind the Jupyter Lab web UI to an available port, if port `8000` is in use.

```python
def find_free_port(start_port=8000) -> int:
    """Find a free port starting from a specific port number."""
    port = start_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind(("0.0.0.0", port))
                return port
            except socket.error:
                print(f"Port {port} is in use, trying the next port.")
                port += 1

```

## Change Jupyter Lab's starting path

You can set the path Jupyter Lab opens in the web UI using `--ServerApp.default_url='/lab?file-browser-path=/path/to/open'`
--ServerApp.default_url="/lab?file-browser-path=/years"

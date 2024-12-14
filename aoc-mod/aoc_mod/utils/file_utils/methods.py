import typing as t
from pathlib import Path
from loguru import logger as log


def load_inputs(inputs_file: t.Union[str, Path] = "inputs"):
    """Load Advent of Code inputs from a file.
    
    Params:
        inputs_file (str, optional): The path to the input file. Defaults to "inputs".
    """
    if not inputs_file:
        raise ValueError("inputs_file cannot be empty")
    inputs_file: Path = Path(str(inputs_file)).expanduser() if "~" in str(inputs_file) else Path(str(inputs_file))
    
    if not inputs_file.exists():
        raise FileNotFoundError(f"inputs_file {inputs_file} does not exist")
    
    log.debug(f"Reading contents of file: {inputs_file}")
    try:
        with open(inputs_file, "r") as f:
            return [line.strip() for line in f.readlines()]
        
    except Exception as exc:
        log.error(f"{type(exc)} Error reading file {inputs_file}: {exc}")
        raise Exception(f"Error reading file {inputs_file}: {exc}")
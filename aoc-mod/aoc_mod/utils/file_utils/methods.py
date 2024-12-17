import typing as t
from pathlib import Path
from loguru import logger as log
import json


def load_inputs(inputs_file: t.Union[str, Path] = "./inputs"):
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
    
    
def save_results(results: dict, output_file: t.Union[str, Path] = "./solutions.json"):
    """Save results to a JSON file."""
    try:
        json_data = json.dumps(results, indent=4)
    except Exception as exc:
        msg = f"({type(exc)}) Error dumping results dict to JSON. Details: {exc}"
        log.error(msg)
        
        raise exc
    
    try:
        with open(output_file, "w") as f:
            f.write(json_data)
    except Exception as exc:
        msg = f"({type(exc)}) Error writing results to file {output_file}. Details: {exc}"
        log.error(msg)
        
        raise exc

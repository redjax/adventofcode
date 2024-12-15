from IPython.display import display
import pandas as pd

def display_df_without_index(df: pd.DataFrame, head: int | None = None, tail: int | None = None) -> None:
    """Display a Pandas DataFrame in a Jupyter notebook, without the DataFrame index column.

    Params:
        df (pandas.DataFrame): The Pandas DataFrame to print without the index column.

    Returns:
        None
    Raises:
        ValueError: When both `head` and `tail` values are passed.

    """
    if head and tail:
        raise ValueError("Cannot pass a value for both head and tail, you must use one or the other.")
    try:
        if head:
            display(df.head(head).style.hide(axis="index"))
        elif tail:
            display(df.tail(tail).style.hide(axis="index"))
        else:
            display(df.style.hide(axis="index"))
    except Exception as exc:
        msg: str = f"({type(exc)}) Error displaying Pandas DataFrame. Details: {exc}"
        print(f"[ERROR] {msg}")

        raise exc

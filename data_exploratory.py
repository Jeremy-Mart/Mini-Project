import pandas as pd

def dataset_info(df: pd.DataFrame) -> None:
    """
    Displays key information about a pandas DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to analyze.

    Outputs
    -------
    - Number of rows and columns.
    - List of column names.
    - Data types of each column.
    """
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}\n")
    
    print("Column names:")
    print(df.columns.tolist(), "\n")
    
    print("Data types:")
    print(df.dtypes, "\n")

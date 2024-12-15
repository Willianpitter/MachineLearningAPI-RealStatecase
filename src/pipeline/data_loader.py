import pandas as pd

def load_data(source: str, is_csv: bool = True) -> pd.DataFrame:
    if is_csv:
        return pd.read_csv(source)
    # Placeholder for DB connection
    raise NotImplementedError("Database connection not implemented.")

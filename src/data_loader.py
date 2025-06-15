import pandas as pd
def load_data(path:str):
    """Load insurance dataset."""
    df=pd.read_csv(path,delimiter="|")
    return df

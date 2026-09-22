import pandas as pd


IRIS_DATA_URL = (
    "https://raw.githubusercontent.com/uiuc-cse/"
    "data-fa14/gh-pages/data/iris.csv"
)

def load_iris_data():
    """
    Load the Iris dataset from the remote CSV source.
    """
    df = pd.read_csv(IRIS_DATA_URL)

    df.insert(0, "id", range(1, len(df) + 1))

    return df
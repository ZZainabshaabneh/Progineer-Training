
import pandas as pd


def load_csv(file):
    """Read a CSV file and return a DataFrame."""
    return pd.read_csv(file)


def get_missing_values(df):
    """Count missing values in each column."""
    return df.isnull().sum()


def get_summary_statistics(df):
    """Calculate summary statistics for numeric columns."""
    numeric_df = df.select_dtypes(include="number")
    return numeric_df.describe()

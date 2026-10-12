
import pandas as pd

from DataExpoler.data_utils import (
    get_missing_values,
    get_summary_statistics,
)


def test_get_missing_values():
    df = pd.DataFrame({
        "Name": ["Sara", "Ahmad"],
        "Age": [20, None],
    })

    result = get_missing_values(df)

    assert result["Name"] == 0
    assert result["Age"] == 1


def test_get_summary_statistics():
    df = pd.DataFrame({
        "Age": [10, 20, 30],
        "Name": ["Sara", "Ahmad", "Lina"],
    })

    result = get_summary_statistics(df)

    assert result.loc["mean", "Age"] == 20
    assert result.loc["min", "Age"] == 10
    assert result.loc["max", "Age"] == 30

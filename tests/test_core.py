import pandas as pd
from datafixer import clean


def test_fix_column_names():
    df = pd.DataFrame({" Name ": [1]})

    result = clean(df).fix_column_names().get()

    assert "name" in result.columns


def test_remove_duplicates():
    df = pd.DataFrame({"name": ["a", "a"]})

    result = clean(df).remove_duplicates().get()

    assert len(result) == 1


def test_fill_missing():
    df = pd.DataFrame({"name": ["a", None]})

    result = clean(df).fill_missing("unknown").get()

    assert result.iloc[1]["name"] == "unknown"


def test_report():
    df = pd.DataFrame({"name": ["Alice", None]})

    report = clean(df).report()

    assert report["rows"] == 2
    assert report["columns"] == 1


def test_standardize_text():
    df = pd.DataFrame({
        "name": [" Alice ", "BOB"]
    })

    result = clean(df).standardize_text().get()

    assert result.iloc[0]["name"] == "alice"
    assert result.iloc[1]["name"] == "bob"


def test_remove_outliers():
    df = pd.DataFrame({
        "salary": [10, 12, 15, 18, 1000]
    })

    result = clean(df).remove_outliers("salary").get()

    assert len(result) == 4

import pandas as pd
import pytest 

from datafixer import clean


def test_summary():
    df = pd.DataFrame({"age": [20, 30, 40], "city": ["A", "B", "C"]})

    result = clean(df).summary()

    assert "age" in result.columns


def test_data_quality_report():
    df = pd.DataFrame({"a": [1, None, 3], "b": [1, 1, 1]})

    report = clean(df).data_quality_report()

    assert report["rows"] == 3
    assert report["columns"] == 2
    assert report["missing_values"] == 1


def test_drop_empty_columns():
    df = pd.DataFrame({"name": ["Alice", "Bob"], "empty": [None, None]})

    result = clean(df).drop_empty_columns().get()

    assert "empty" not in result.columns


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
    df = pd.DataFrame({"name": [" Alice ", "BOB"]})

    result = clean(df).standardize_text().get()

    assert result.iloc[0]["name"] == "alice"
    assert result.iloc[1]["name"] == "bob"


def test_remove_outliers():
    df = pd.DataFrame({"salary": [10, 12, 15, 18, 1000]})

    result = clean(df).remove_outliers("salary").get()

    assert len(result) == 4



def test_remove_outliers_invalid_column():
    df = pd.DataFrame({"salary": [10, 20, 30]})

    with pytest.raises(ValueError):
        clean(df).remove_outliers("age")


def test_empty_dataframe():
    df = pd.DataFrame()

    result = clean(df).get()

    assert result.empty


def test_remove_duplicates_no_duplicates():
    df = pd.DataFrame({"a": [1, 2, 3]})

    result = clean(df).remove_duplicates().get()

    assert len(result) == 3


def test_fill_missing_replaces_nulls():
    df = pd.DataFrame({"a": [1, None, 3]})

    result = clean(df).fill_missing(0).get()

    assert result["a"].isna().sum() == 0


def test_data_quality_report_empty():
    df = pd.DataFrame()

    report = clean(df).data_quality_report()

    assert report["rows"] == 0
    assert report["columns"] == 0


def test_summary_returns_dataframe():
    df = pd.DataFrame({"a": [1, 2, 3]})

    result = clean(df).summary()

    assert isinstance(result, pd.DataFrame)

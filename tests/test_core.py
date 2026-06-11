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

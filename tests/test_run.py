import pandas as pd
from datafixer import clean

df = pd.DataFrame({
    " Name ": ["A", None, "C"],
    " Age ": [20, 30, None]
})

result = clean(df).fix_column_names().remove_nulls().get()

print(result)

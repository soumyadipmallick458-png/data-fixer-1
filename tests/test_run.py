import pandas as pd
from datafixer import clean

df = pd.DataFrame({
    " Name ": [" Alice ", " Bob ", " Bob ", None],
    " Age ": [20, None, None, 30]
})

result = (
    clean(df)
    .fix_column_names()
    .strip_text()
    .lowercase_text()
    .fill_missing("unknown")
    .remove_duplicates()
    .get()
)

print(result)

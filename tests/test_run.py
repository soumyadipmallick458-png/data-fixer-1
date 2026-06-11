import pandas as pd
from datafixer import clean

df = pd.DataFrame({
    " Name ": [" Alice ", " Bob ", " Bob ", None],
    " Sales ": [10, 20, 20, 1000]
})

result = (
    clean(df)
    .fix_column_names()
    .standardize_text()
    .remove_duplicates()
    .remove_outliers("sales")
    .get()
)

print(result)

print("\nSummary:")
print(clean(result).summary())

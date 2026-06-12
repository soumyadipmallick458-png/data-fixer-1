import pandas as pd
from datafixer import clean

df = pd.DataFrame({
    " Name ": [" Alice ", " Bob ", None],
    " Sales ": [10, 20, 1000]
})

result = (
    clean(df)
    .fix_column_names()
    .remove_duplicates()
    .standardize_text()
    .remove_outliers("sales")
    .get()
)

print(result)

report = clean(df).data_quality_report()

print(report)

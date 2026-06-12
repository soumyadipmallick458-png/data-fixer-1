# DataFixer

Description

DataFixer is a lightweight Python library built on top of pandas that provides chainable data-cleaning and data-quality utilities for faster exploratory data analysis.


## Features

- Clean column names
- Remove missing values
- Fill missing values
- Remove duplicate rows
- Standardize text columns
- Remove empty strings
- Drop empty columns
- Sort data
- Remove outliers using IQR
- Generate dataset summaries
- Generate data quality reports

## Installation

```bash
pip install git+https://github.com/soumyadipmallick458-png/data-fixer-1.git
```

## Quick Start

This example cleans column names, removes duplicates, standardizes text values, removes outliers, and generates a data quality report.

```python
import pandas as pd
from datafixer import clean

df = pd.DataFrame({
    " Name ": [" Alice ", " Bob ", None],
    " Sales ": [10, 20, 1000]
})

cleaner = (
    clean(df)
    .fix_column_names()
    .remove_duplicates()
    .standardize_text()
    .remove_outliers("sales")
)

result = cleaner.get()
report = cleaner.data_quality_report()

print(result)
print(report)
```
## License

MIT License



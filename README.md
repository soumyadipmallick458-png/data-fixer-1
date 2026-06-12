# DataFixer

DataFixer is a lightweight Python library built on top of pandas that provides chainable data-cleaning utilities for faster exploratory data analysis.

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

## Installation

```bash
pip install -e

## Quick Start

```python
import pandas as pd
from datafixer import clean

df = pd.DataFrame({
    " Name ": [" Alice ", " Bob ", None],
    " Sales ": [10, 20, 1000]
})

result = (
    clean(df)
    .fix_column_names()
    .standardize_text()
    .remove_outliers("sales")
    .get()
)

print(result)
```

import pandas as pd

class Clean:

    def summary(self) -> pd.DataFrame:
        return self.df.describe(include="all")


    def data_quality_report(self) -> dict:
        return {
        "rows": len(self.df),
        "columns": len(self.df.columns),
        "missing_values": int(self.df.isna().sum().sum()),
        "duplicate_rows": int(self.df.duplicated().sum()),
        "missing_by_column": (
            self.df.isna()
            .sum()
            .to_dict()
        )
    }

    def __init__(self, df):
        self.df = df.copy()

    def remove_duplicates(self) -> "clean":
        self.df = self.df.drop_duplicates()
        return self

    def fill_missing(self, value) -> "clean":
        self.df = self.df.fillna(value)
        return self

    def lowercase_text(self):
        for col in self.df.select_dtypes(include="object"):
            self.df[col] = self.df[col].str.lower()
        return self

    def strip_text(self):
        for col in self.df.select_dtypes(include="object"):
            self.df[col] = self.df[col].str.strip()
        return self

    def fix_column_names(self):
        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_", regex=False)
        )
        return self

    def standardize_text(self) -> "clean":
        for col in self.df.select_dtypes(include=["object", "string"]):
            self.df[col] = (
                self.df[col]
                .str.strip()
                .str.lower()
            )
        return self

    def report(self):
        return {
            "rows": len(self.df),
            "columns": len(self.df.columns),
            "missing_values": int(self.df.isna().sum().sum()),
            "duplicate_rows": int(self.df.duplicated().sum())
        }


    def remove_outliers(self, column: str) -> "clean":
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found")


        q1 = self.df[column].quantile(0.25)
        q3 = self.df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        self.df = self.df[
            (self.df[column] >= lower)
            & (self.df[column] <= upper)
        ]

        return self

    def drop_empty_columns(self):
        self.df = self.df.dropna(axis=1, how="all")
        return self


    def get(self) -> pd.DataFrame:
        return self.df



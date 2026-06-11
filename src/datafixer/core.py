import pandas as pd


class Clean:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def remove_nulls(self):
        self.df = self.df.dropna()
        return self

    def fix_column_names(self):
        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )
        return self

    def remove_duplicates(self):
        self.df = self.df.drop_duplicates()
        return self

    def fill_missing(self, value):
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

    def standardize_text(self):
        for col in self.df.select_dtypes(include="object"):
            self.df[col] = (
                self.df[col]
                .str.strip()
                .str.lower()
            )
        return self

    def remove_empty_strings(self):
        self.df = self.df.replace(r"^\s*$", pd.NA, regex=True)
        self.df = self.df.dropna()
        return self

    def drop_empty_columns(self):
        self.df = self.df.dropna(axis=1, how="all")
        return self

    def rename_columns(self, mapping):
        self.df = self.df.rename(columns=mapping)
        return self

    def sort_by(self, column, ascending=True):
        self.df = self.df.sort_values(
            by=column,
            ascending=ascending
        )
        return self

    def remove_outliers(self, column):
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

    def summary(self):
        return {
            "rows": len(self.df),
            "columns": len(self.df.columns),
            "missing_values": int(
                self.df.isna().sum().sum()
            )
        }

    def get(self):
        return self.df

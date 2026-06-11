
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

    def get(self):
        return self.df

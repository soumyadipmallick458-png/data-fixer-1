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

    def get(self):
        return self.df

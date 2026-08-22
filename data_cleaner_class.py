import seaborn as sns


class DataCleaner:
    """
    Wraps common EDA cleaning steps (filling missing values, dropping columns,
    filtering rows) as reusable methods on a DataFrame, so the same cleaning
    logic can be applied across different datasets without rewriting the same
    pandas lines each time.
    """

    def __init__(self, df):
        self.df = df

    def fill_missing(self, column, strategy="median"):
        # strategy is a parameter rather than hardcoded so the same method
        # works for both numeric columns (median/mean) and categorical
        # columns (mode) - median is the default since it's the more common
        # choice and is resistant to outliers skewing the fill value.
        if strategy == "median":
            fill_value = self.df[column].median()
        elif strategy == "mode":
            fill_value = self.df[column].mode()[0]
        elif strategy == "mean":
            fill_value = self.df[column].mean()
        else:
            print(f"Unknown strategy: {strategy}")
            return
        self.df[column] = self.df[column].fillna(fill_value)

    def drop_column(self, column):
        self.df = self.df.drop(columns=[column])

    def filter_rows(self, column, condition, value):
        if condition == "=":
            self.df = self.df[self.df[column] == value]
        elif condition == ">":
            self.df = self.df[self.df[column] > value]
        elif condition == "<":
            self.df = self.df[self.df[column] < value]
        elif condition == "!=":
            self.df = self.df[self.df[column] != value]
        else:
            print("Invalid Condition")
            return

    def summary(self):
        print(self.df.isnull().sum())


df = sns.load_dataset("titanic")

cleaner = DataCleaner(df.copy())  # .copy() so the original df is left untouched
cleaner.summary()  # see missing values before cleaning

cleaner.fill_missing("age", strategy="median")
cleaner.fill_missing("embarked", strategy="mode")
cleaner.fill_missing("embark_town", strategy="mode")  # separate column from
# "embarked" - same info in a different format (full name vs. letter code),
# so it needs to be filled separately
cleaner.drop_column("deck")  # ~77% missing, too sparse to fill reliably

cleaner.summary()  # confirm missing values are gone

cleaner.filter_rows("pclass", "=", 1)
print(cleaner.df.shape)  # confirm the filter worked
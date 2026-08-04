import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class DataCleaner:
    def __init__(self, df):
        self.df = df
    def fill_missing(self, column, strategy="median"):
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

cleaner = DataCleaner(df.copy())
cleaner.summary()          # see missing values before cleaning
cleaner.fill_missing("age", strategy="median")
cleaner.fill_missing("embarked", strategy="mode")
cleaner.fill_missing("embark_town", strategy="mode")
cleaner.drop_column("deck")
cleaner.summary()          # confirm missing values are gone
cleaner.filter_rows("pclass", "=", 1)
print(cleaner.df.shape)    # confirm the filter worked
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")
age_median = df["age"].median()
df["age"] = df["age"].fillna(age_median)
df = df.drop(columns=["deck"])
most_common = df["embarked"].mode()[0]
df["embarked"] = df["embarked"].fillna(most_common)
most_common_town = df["embark_town"].mode()[0]
df["embark_town"] = df["embark_town"].fillna(most_common_town)
df["age"].hist(bins=20)
print(df.groupby(["pclass","sex"])["survived"].mean()) 
"""After calculating percantages using the given date it was found that the strongest
factor in surviving was gender. The numbers showed that being a woman made it much more likely to survive
than it was for men. Also the class in which they were mattered as the survival rate in the 1st class was higher than both
the 2nd and 3rd class."""
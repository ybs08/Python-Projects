import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")

# age: ~20% missing, enough to justify filling rather than dropping those
# rows. Median used instead of mean since it's more resistant to outliers.
age_median = df["age"].median()
df["age"] = df["age"].fillna(age_median)

# deck: ~77% missing - too sparse to fill reliably, so the whole column is
# dropped instead of guessing at values for the vast majority of rows.
df = df.drop(columns=["deck"])

# embarked / embark_town: same boarding info in two formats (letter code vs.
# full name), each with only 2 missing values - filled separately since
# they're two different columns, not just one.
most_common = df["embarked"].mode()[0]
df["embarked"] = df["embarked"].fillna(most_common)
most_common_town = df["embark_town"].mode()[0]
df["embark_town"] = df["embark_town"].fillna(most_common_town)

df["age"].hist(bins=20)
plt.title("Age Distribution")
plt.show()

print(df.groupby(["pclass", "sex"])["survived"].mean())

"""
After calculating survival percentages, gender was found to be the strongest
factor: women survived at much higher rates than men. Class also mattered -
survival rate in 1st class was higher than both 2nd and 3rd. Notably, these
two factors combine rather than acting independently: even a 3rd class woman
(50% survival) was more likely to survive than a 1st class man (37%), and
class affected women's survival odds far more sharply than men's (97% -> 50%
across classes for women, vs. 37% -> 14% for men).
"""
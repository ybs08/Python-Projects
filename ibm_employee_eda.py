import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Two columns are constant across every row (no variation at all), so they're
# useless for analysis/correlation - confirmed with .unique() before dropping.
# EmployeeCount is always 1, StandardHours is always 80.
df = df.drop(columns=["EmployeeCount", "StandardHours"])

# Compare a handful of likely "seniority" factors between employees who left
# vs. stayed. Looking at medians rather than means since a few outliers
# shouldn't be allowed to skew the comparison.
columns_to_check = ["JobLevel", "YearsAtCompany", "DistanceFromHome", "StockOptionLevel", "TrainingTimesLastYear"]
print(df.groupby("Attrition")[columns_to_check].median())

# JobLevel and YearsAtCompany are checked against each other because they
# looked like they might be measuring the same underlying thing (seniority)
# rather than two independent factors. A correlation of ~0.53 confirms they
# move together fairly strongly, so they shouldn't be treated as separate,
# independent causes of attrition.
print(df["YearsAtCompany"].corr(df["JobLevel"]))

# Convert Attrition to 0/1 so it can be used in a numeric correlation check.
df["Attrition_numeric"] = df["Attrition"].map({"Yes": 1, "No": 0})

# Check every numeric column's correlation with attrition at once, rather
# than testing columns one at a time - a faster, more systematic way to
# scan a wide dataset for patterns worth digging into further.
correlations = df.corr(numeric_only=True)["Attrition_numeric"].sort_values()
print(correlations)

"""
Finding: employees who left tend to be less senior overall - lower JobLevel,
fewer YearsAtCompany, lower MonthlyIncome, and lower StockOptionLevel than
those who stayed. These aren't independent signals: YearsAtCompany and
JobLevel alone correlate at ~0.53, meaning they largely reflect the same
underlying trait (seniority/tenure) rather than separate causes. The full
correlation scan confirms this - TotalWorkingYears, JobLevel, YearsInCurrentRole,
MonthlyIncome, Age, YearsWithCurrManager, StockOptionLevel, and YearsAtCompany
all cluster together with similar, moderate negative correlations to attrition.
None of these correlations are individually strong (all roughly -0.13 to -0.17),
so seniority is a real factor but far from the only one. BusinessTravel showed
no meaningful difference between groups and does not appear to be a real
factor. DistanceFromHome showed a small positive correlation (further from
home is weakly associated with leaving more).
"""


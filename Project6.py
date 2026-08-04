import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel("نتيجة ثانوية عامة نظام حديث.xlsx")
print(df["student_case_desc"].unique())
df = df[(df["total_degree"] >= 160) & (df["student_case_desc"] == "ناجح دور أول")]
df = df.drop(columns=["seating_no"])
print(df.columns.tolist())
print(df.describe())
df["total_degree"].hist(bins=20)
plt.title("Total Degrees")
plt.show()

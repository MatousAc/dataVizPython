import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv("sauFinal.csv")
# df["test"] = [1 for x in df["L: "]]
print(df.head(10))
print(df.columns)

# dataPoints = pd.crosstab(index = df["deptCode"], columns="count")
sns.barplot(x="deptCode", y="minCredit", data=df, estimator=sum)
plt.show()
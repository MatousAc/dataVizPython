import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv('earthquakes.csv')
df["test"] = random.random()  #1 if ("I") else 2 if ("R") else 3 if ("M") else 0
print(df.head(10))
print(df.columns)

# dataPoints = pd.crosstab(index = df["deptCode"], columns="count")
sns.barplot(x="deptCode", y="minCredit", data=df, estimator=sum)
plt.show()
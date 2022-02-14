import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolours
import random

df = pd.read_csv("sauFinal.csv")
df["#of rows"] = [1 for x in df["courseID"]]
print(df.head(10))
print(df.columns)

# dataPoints = pd.crosstab(index = df["deptCode"], columns="count")

sns.barplot(x="#of rows", y="deptCode", 
	# hue="# of rows",
	data=df, 
	order=[
		"HPER",
		"BUS",
		"ART",
		"HIST",
		"REL",
		"JOUR",
		"MDLG",
		"MUS",
		"ENGL",
		"TECH",
		"BIOL",
		"EDUC",
		"SWFS",
		"PSYC",
		"PHYS",
		"CPTR",
		"CHEM",
		"NRSG",
		"MATH",
		"PTAP",
		"ALHL"
		],
	estimator=sum,
	palette=sns.color_palette("mako")
	).set(title="Responsiveness by Department")

plt.show()
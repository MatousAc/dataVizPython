from asyncio.windows_events import NULL

from numpy import average
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolours

df = pd.read_csv("sauFinal.csv")
df["L: Effective Communication"].replace({NULL: 0, "I": 1, "R": 2, "M": 3}, inplace=True)
df["L:  Critical Thinking"].replace({NULL: 0, "I": 1, "R": 2, "M": 3}, inplace=True)
df["L: Decision Making"].replace({NULL: 0, "I": 1, "R": 2, "M": 3}, inplace=True)
df["L: Empathy"].replace({NULL: 0, "I": 1, "R": 2, "M": 3}, inplace=True)
df["L: Strategic Thinking"].replace({NULL: 0, "I": 1, "R": 2, "M": 3}, inplace=True)

leadCols = ["L: Effective Communication", "L:  Critical Thinking", 
	"L: Decision Making", "L: Empathy", "L: Strategic Thinking"]
df["Leadership Score"] = df[leadCols].sum(axis=1)

# df = df.sort_values("Leadership", ascending=True)
# dataPoints = pd.crosstab(index = df["deptCode"], columns="count")

sns.barplot(x="Leadership Score", y="deptCode", 
	# hue="# of rows",
	data=df, 
	order=[
		"HPER",
		"ART",
		"HIST",
		"JOUR",
		"ENGL",
		"MUS",
		"BUS",
		"SWFS",
		"EDUC",
		"TECH",
		"MDLG",
		"REL",
		"PTAP",
		"BIOL",
		"MATH",
		"CHEM",
		"CPTR",
		"PSYC",
		"PHYS",
		"NRSG",
		"ALHL"
		],
	estimator=average,
	color="green",
	).set(title="Leadership by Department")

plt.show()
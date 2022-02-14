from asyncio.windows_events import NULL

from numpy import average
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolours

df = pd.read_csv("sauFinal.csv")
df["CPS: Clarification"].replace({NULL: 0, "I": 1, "R": 2, "M": 3}, inplace=True)
df["CPS: Ideation"].replace({NULL: 0, "I": 1, "R": 2, "M": 3}, inplace=True)
df["CPS: Solution Development"].replace({NULL: 0, "I": 1, "R": 2, "M": 3}, inplace=True)
df["CPS: Implementation"].replace({NULL: 0, "I": 1, "R": 2, "M": 3}, inplace=True)

leadCols = ["CPS: Clarification", "CPS: Ideation", "CPS: Solution Development", "CPS: Implementation",]
df["Creativity Score"] = df[leadCols].sum(axis=1)

sns.barplot(x="Creativity Score", y="deptCode", 
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
	color="red",
	).set(title="Creativity by Department")

plt.show()

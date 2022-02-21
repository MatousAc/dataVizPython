from asyncio.windows_events import NULL
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolours

sau = pd.read_csv("sauFinal.csv")

for col in sau.columns:
	sau[col].replace({NULL: 0, "I": 1, "R": 2, "M": 3}, inplace=True)

irm = pd.DataFrame()
irm["level"] = ["None", "Introduced", "Reinforced", "Mastered"]
irm["count"] = 0

for col in sau.columns:
	countI = 0
	countR = 0
	countM = 0
	countN = 0
	for val in sau[col]:
		if val == "I":
			countI += 1
		elif val == "R":
			countR += 1
		elif val == "M":
			countM += 1
		else:
			countN += 1
	
	
		
		
			

leadCols = ["CPS: Clarification", "CPS: Ideation", "CPS: Solution Development", "CPS: Implementation",]
sau["Creativity Score"] = sau[leadCols].sum(axis=1)

sns.barplot(x="Creativity Score", y="deptCode", 
	# hue="# of rows",
	data=sau, 
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
	estimator=sum,
	color="red",
	).set(title="Creativity by Department")

plt.show()
from asyncio.windows_events import NULL
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolours

df = pd.read_csv("sauFinal.csv")

df["Creativity Score"] = df[leadCols].sum(axis=1)

sns.barplot(x="Creativity Score", y="deptCode", 
	# hue="# of rows",
	data=df,
	estimator=sum,
	color="red",
	).set(title="Creativity by Department")

plt.show()
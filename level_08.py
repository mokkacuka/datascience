# INPUT A CSV FILE CONTAINING CATEGORICAL AND QUANTITATIVE VARIABLES
# DRAW A CATEGORICAL SCATTER PLOT

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

df = pd.read_csv('yourFile.csv')
df

#Turn column's values from str to int - Not mandatory (depends on source variable's format)
#Replace someVariable with a variable from source file
df.someVariable = pd.to_numeric(df.someVariable)

#Categorical Scatter Plot : Likes per Category
sns.catplot(x="myQuantitativeVariable", y="myCategoricalVariable", data=df, jitter=False);

plt.show()

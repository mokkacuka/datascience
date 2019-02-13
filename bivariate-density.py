# INPUT A CSV FILE
# DRAW A DENSITY MAP FROM TWO QUANTITATIVE VARIABLES

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

sns.set(color_codes=True)

# Import CSV file and create Dataframe
df = pd.read_csv('2018-CONSOLIDATED_Organic.csv')
df

# Turn column's values from str to int - Not mandatory (depends on source variables' format) 
df.myVariable1 = pd.to_numeric(df.myVariable1)
df.myVariable2 = pd.to_numeric(df.myVariable2)

f, ax = plt.subplots(figsize=(6, 6))
cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
sns.kdeplot(df.myVariable1, df.myVariable2, cmap=cmap, n_levels=60, shade=True);

plt.show()

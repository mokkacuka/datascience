# INPUT A CSV FILE

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

sns.set(color_codes=True)

df = pd.read_csv('2018-CONSOLIDATED_Organic.csv')
df

#Turn column's values from str to int
df.AverageViewPercentage = pd.to_numeric(df.AverageViewPercentage)
df.Likes = pd.to_numeric(df.Likes)

#sns.jointplot(x=df.AverageViewPercentage , y=df.LikesPerDay, data=df);

f, ax = plt.subplots(figsize=(6, 6))
cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
sns.kdeplot(df.AverageViewPercentage, df.Likes, cmap=cmap, n_levels=60, shade=True);

plt.show()

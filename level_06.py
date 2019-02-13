#
# IMPORT CSV FILE INTO A DATAFRAME
# DRAW A PLOT FROM TWO VARIABLES OF DATAFRAME
#

# Import all libraries needed for the tutorial
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Create a Dataframe from an input CSV file
df = pd.read_csv('2018EXTENDED-Organic.csv')
df

# Round a variable of the Dataframe
df.AverageViewPercentage.apply(np.round)

# Turn column's values from str to int
df.Likes = pd.to_numeric(df.Likes)

# Get the maximum value of the variable and add 10%
maxValueX = df.AverageViewPercentage.max()
maxValueY = df.Likes.max()

# Draw median
plt.axvline(56, color='r')
plt.axhline(93, color='r')

plt.plot(df.AverageViewPercentage, df.Likes, 'ro', c='black')
plt.axis([0, maxValueX, 0, maxValueY])
plt.xlabel('Average Watched Percentage')
plt.ylabel('Likes')
plt.show()

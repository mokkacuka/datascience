# IMPORT CSV FILE INTO A DATAFRAME
# DRAW A PLOT FROM TWO VARIABLES OF DATAFRAME

# Import all libraries needed for the tutorial
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Create a Dataframe from a source CSV file
df = pd.read_csv('yourFile.csv')
df

# Round a variable of the Dataframe - Not mandatory (depends on variable type)
# Replace variable1 by the name of a variable of source file
df.variable1.apply(np.round)

# Turn column's values from str to int - Not mandatory (depends on variable type)
# Replace variable1 by the name of a variable of source file
df.variable2 = pd.to_numeric(df.Likes)

# Get the maximum value of the variable and add 10%
maxValueX = df.variable1.max()
maxValueY = df.variable2.max()

# Draw median (median values have beeen calculated externally) - Not mandatory
plt.axvline(56, color='r')
plt.axhline(93, color='r')

plt.plot(df.variable1, df.variable2, 'ro', c='black')
plt.axis([0, maxValueX, 0, maxValueY])
plt.xlabel('Variable1')
plt.ylabel('Variable2')
plt.show()

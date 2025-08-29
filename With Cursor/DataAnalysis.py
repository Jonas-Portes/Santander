# Basic Data Analysis

#Calculate simple statistics: mean, median, standard deviation for each column.
#Generate a scatter plot of one column vs. the other (here you will have to use matplotlib; try asking Cursor "Plot a scatter plot of col1 vs. col2").
#See how the AI can even write Matplotlib code for you.
#Run the script; if you are in Cursor, the graph should open in an external window (or in the VS Code plot pane if enabled).
#This exercise mixes programming with a touch of data science, showcasing Cursor's versatility.



import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('small_dataset.csv')

mean = df.mean()
median = df.median()
standard_deviation = df.std()


# Scatter plot of col1 vs. col2 (fallback to first two numeric columns)
if {'col1', 'col2'}.issubset(df.columns):
    x_col, y_col = 'col1', 'col2'
else:
    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) < 2:
        raise ValueError('Need at least two numeric columns to plot.')
    x_col, y_col = num_cols[:2]

plt.figure()
plt.scatter(df[x_col], df[y_col], alpha=0.7)
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.title(f'Scatter plot: {x_col} vs {y_col}')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
plt.tight_layout()
plt.show()
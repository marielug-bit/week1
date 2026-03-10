import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-darkgrid')
#%matplotlib inline
pd.set_option('display.max_rows', 100)

flights = sns.load_dataset('flights')
print("Loaded!")

print(flights.head())
print(flights[flights['year']==1955]['month'])


print(flights[(flights['month'].isin(['Mar','Apr','May']))&(flights['passengers'].between(200, 400))])

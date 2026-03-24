# Data Import and Cleaning:

# Import the dataset using Pandas.
# Identify missing values and handle them appropriately.
# Use NumPy to convert relevant columns to numerical types if necessary.
from scipy.stats import ttest_ind, f_oneway
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
df_original = pd.read_csv('/Users/mariekrammer/Desktop/DI learning/week_4_ML_AI/day_2/global_power_plant_database.csv')

#print(df_original.head())
#print(df.shape)
#print(df.info())
print(df_original.columns)
#print(df.describe())

print(df_original[df_original.duplicated()]) #no duplicates
print((df_original.isnull().sum()/len(df_original))*100)

#print(df_original[df_original['generation_gwh_2013'].isnull()]['estimated_generation_gwh_2013'])

df= df_original.copy()
df['generation_gwh_2013'] = np.where(df['generation_gwh_2013'].notna(),df['generation_gwh_2013'],df['estimated_generation_gwh_2013'])
df['generation_gwh_2014'] = np.where(df['generation_gwh_2014'].notna(),df['generation_gwh_2014'],df['estimated_generation_gwh_2014'])
df['generation_gwh_2015'] = np.where(df['generation_gwh_2015'].notna(),df['generation_gwh_2015'],df['estimated_generation_gwh_2015'])
df['generation_gwh_2016'] = np.where(df['generation_gwh_2016'].notna(),df['generation_gwh_2016'],df['estimated_generation_gwh_2016'])
df['generation_gwh_2017'] = np.where(df['generation_gwh_2017'].notna(),df['generation_gwh_2017'],df['estimated_generation_gwh_2017'])

df = df.drop(columns=['other_fuel1','other_fuel2','other_fuel3','commissioning_year','wepp_id',
                                'year_of_capacity_data','estimated_generation_gwh_2013', 'estimated_generation_gwh_2014', 
                                'estimated_generation_gwh_2015','estimated_generation_gwh_2016','estimated_generation_gwh_2017',
                                'generation_data_source','generation_gwh_2018','generation_gwh_2019'])

df.info()

#print((df.isnull().sum()/len(df))*100)

#print(df.groupby('country')['owner'].apply(list))
#df['owner']=df['owner'].fillna(df.groupby('country')['owner'].transform(lambda x:x.mode()))
df['owner'] = df['owner'].fillna(
    df.groupby('country')['owner'].transform(
        lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan
    )
)
df['owner'] = df['owner'].fillna(df['owner'].mode().iloc[0])
df = df[df['source'].notna()]
df = df[df['url'].notna()]
df = df[df['geolocation_source'].notna()]
#print((df.isnull().sum()/len(df))*100)

median = df['generation_gwh_2013'].median()
df['generation_gwh_2013'] = df['generation_gwh_2013'].fillna(median)

median = df['generation_gwh_2014'].median()
df['generation_gwh_2014'] = df['generation_gwh_2014'].fillna(median)

median = df['generation_gwh_2015'].median()
df['generation_gwh_2015'] = df['generation_gwh_2015'].fillna(median)

median = df['generation_gwh_2016'].median()
df['generation_gwh_2016'] = df['generation_gwh_2016'].fillna(median)

df = df[df['generation_gwh_2017'].notna()]


print((df.isnull().sum()/len(df))*100)




# Exploratory Data Analysis:

# Utilize Pandas to summarize key statistics (mean, median, standard deviation) for numerical columns.
# Explore the distribution of power plants by country and fuel type.

print(df.describe())

print(df['country'].nunique())

plants_by_country = df['country_long'].value_counts()

print(plants_by_country.head(10))

plants_by_country.head(10).plot(kind='bar')
plt.title("Top 10 countries by number of power plants")
plt.xlabel("Country")
plt.ylabel("Number of plants")
plt.show()

fuel_distribution = df['primary_fuel'].value_counts()

print(fuel_distribution)

fuel_distribution.plot(kind='bar')
plt.title("Distribution of power plants by fuel type")
plt.xlabel("Fuel type")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# Statistical Analysis:

# Perform a statistical analysis of power output by fuel type using NumPy’s statistical functions.
# Use hypothesis testing to determine if the mean power output differs significantly between different fuel types.

#print(df.groupby('primary_fuel')['capacity_mw'].mean())
# Convert to numpy
fuel = df['primary_fuel'].to_numpy()
capacity = df['capacity_mw'].to_numpy()
print(fuel)
print(capacity)

# Trouver les catégories uniques
unique_fuels = np.unique(fuel)

# mean, median
result_mean = {}
result_median = {}
result_std = {}

for f in unique_fuels:
    result_mean[f] = np.mean(capacity[fuel == f])
    result_median[f] = np.median(capacity[fuel == f])
    result_std[f] = np.std(capacity[fuel == f])

print(result_mean)
print(result_median)
print(result_std)

#Nul hypothesis there is no difference beatween the fuels

groups = []

for f in unique_fuels:
    groups.append(capacity[fuel == f])

print(groups)
#f_stat, p_value = f_oneway()




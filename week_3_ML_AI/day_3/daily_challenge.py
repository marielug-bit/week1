import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.max_colwidth',None)
pd.set_option('display.max_rows',None)
from sklearn.impute import SimpleImputer
from scipy import stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_original = pd.read_csv('/Users/mariekrammer/Desktop/DI learning/week_3_ML_AI/day_3/Airplane_Crashes_and_Fatalities_Since_1908_t0_2023.csv',encoding="latin1")

#print(df_original.head(20))
#print(df_original.shape)
#print(df_original.columns)
print(df_original.info())
print((df_original.isnull().sum()/4998)*100)

#print(df_original.describe())
#print(df_original.isnull().sum())

print(df_original[df_original.duplicated() == True])
print(df_original.duplicated().sum())
print(df_original.nunique())

#duplicates = df[df.duplicated(subset =['Registration'],keep=False)]
#duplicates = duplicates.sort_values(by='Registration')
#print(duplicates)

#Chaque ligne a l air d etre unique

df = df_original.copy()

df = df.drop(columns=['Flight #'])

#30% of col time missing
#print(df['Time'])
#print(df.loc[df['Time'] == '91:05:00'])
df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors= 'coerce')
print(df.head(20))


median = df['Time'].median()
#print(df[df['Time'].isna()])
df['Time'] = df['Time'].fillna(median)
#print(df[df['Time'].isna()])


# supprimer les lignes de data avec petits pourcentages de missing values
#print(df.loc[df['Location'] == 'NaN' ])
#remplir la ou on peut les aboard
print(df.info())

#print(df[df['Aboard'] == 0])
df.loc[df['Aboard'] == 0, 'Aboard'] += 1

df.loc[(df['Aboard'].isna()) | (df['Aboard']==0)& ((df['Aboard Passangers'].notna()) & (df['Aboard Crew'].notna())),'Aboard'] = df['Aboard Passangers']+df['Aboard Crew']
df.loc[(df['Aboard Passangers'].isna()) & (df['Aboard'].notna()) & (df['Aboard Crew'].notna()), 'Aboard Passangers'] = df['Aboard']-df['Aboard Crew']
df.loc[(df['Aboard Crew'].isna()) & (df['Aboard'].notna()) & (df['Aboard Passangers'].notna()), 'Aboard Crew' ] = df['Aboard Passangers']-df['Aboard Passangers']

df.loc[(df['Fatalities'].isna()) & (df['Fatalities Passangers'].notna()) & (df['Fatalities Crew'].notna()),'Fatalities'] = df['Fatalities Passangers']+df['Fatalities Crew']
df.loc[(df['Fatalities Passangers'].isna()) & (df['Fatalities'].notna()) & (df['Fatalities Crew'].notna()), 'Fatalities Passangers'] = df['Fatalities']-df['Fatalities Crew']
df.loc[(df['Fatalities Crew'].isna()) & (df['Fatalities'].notna()) & (df['Fatalities Passangers'].notna()), 'Fatalities Crew' ] = df['Fatalities Passangers']-df['Fatalities Passangers']

#A FAIRE :on pourrait aussi remplir les locations avec Route


print(df.info())
df = df.dropna(subset=['Location','Operator','AC Type','Aboard','Aboard Passangers', 'Aboard Crew','Fatalities','Fatalities Crew','Fatalities Passangers','Ground'])


#creation d une nouvelle colonne Survivors et annee
df['Survivors'] = df['Aboard']-df['Fatalities']
df['Year'] = df['Date'].dt.year

#print(df['Route'].unique())

#imputer la colonne Route Registration cn\ln
imputer = SimpleImputer(strategy='most_frequent')
df[['Route','Registration','cn/ln']]=imputer.fit_transform(df[['Route','Registration','cn/ln']])
print(df.info())


print(df.sort_values('Location',ascending = False).head(10))
#print(df.sort_values('Fatalities',ascending = False).head(10))
#Registration_Imputer = SimpleImputer(strategy='mode')



#print(df.loc[df['Route'].isna()],['Summary'])




#===================================================
#2. EDA Exploratory Data Analysis:
#===================================================

num_crashes = df.shape[0]
print("Total number of crashes:", num_crashes)

total_fatalities = df['Fatalities'].sum()
print("Total fatalities:", total_fatalities)

total_survivors = df['Survivors'].sum()
print("Total survivors:", total_survivors)

survival_rate = total_survivors / df['Aboard'].sum()
print("Survival rate:", survival_rate* 100, "%")

print(df[['Aboard','Fatalities','Survivors']].describe())

crashes_per_year = df.groupby('Year').size()
crashes_per_year.plot()
plt.show()


fatalities_per_year = df.groupby('Year')['Fatalities'].sum()

fatalities_per_year.plot()
plt.title("Fatalities per Year")
plt.show()


#=======================================================
# Statistical Analysis:
#======================================================

mean_fatalities = stats.tmean(df['Fatalities'])
median_fatalities = np.median(df['Fatalities'])
std_fatalities = stats.tstd(df['Fatalities'])

print("Fatalities statistics")
print("Mean:", mean_fatalities)
print("Median:", median_fatalities)
print("Std:", std_fatalities)


mean_survival = stats.tmean(df['Survivors'])
median_survival = np.median(df['Survivors'])
std_survival = stats.tstd(df['Survivors'])

print("Survival rate statistics")
print("Mean:", mean_survival)
print("Median:", median_survival)
print("Std:", std_survival)


##############################################
#3)Statistical analysis
#There is no difference in the mean number of fatalities between the two regions.

Alternative hypothesis (H1)

df['Country'] = df['Location'].str.split(',').str[-1].str.strip()
print(df['Country'].unique())

us_states = [
'Virginia','New Jersey','Ohio','Pennsylvania','Indiana','Iowa','Illinois',
'Wyoming','Wisconsin','Nevada','Texas','Washington','Tennessee','California',
'Florida','Michigan','Arkansas','Colorado','Georgia','Montana','Mississippi'
]

df.loc[df['Country'].isin(us_states),'Country'] = 'United States'

df['Country'] = df['Country'].replace({
    'UK':'United Kingdom',
    'England':'United Kingdom',
    'Scotland':'United Kingdom',
    'Wales':'United Kingdom',
    'USSR':'Russia',
    'Soviet Union':'Russia'
})

df = df[~df['Country'].str.contains('Ocean|Sea|Gulf', na=False)]

print(df['Country'].value_counts().head(20))

def region(country):
    if country == 'United States':
        return 'USA'
    elif country in ['France','Germany','United Kingdom','Italy','Spain']:
        return 'Europe'
    else:
        return 'Other'


df['Region'] = df['Country'].apply(region)
europe = df[df['Region']=='Europe']['Fatalities']
usa = df[df['Region']=='USA']['Fatalities']

from scipy.stats import ttest_ind
t_stat, p_value = ttest_ind(usa.dropna(), europe.dropna())

print(t_stat, p_value)

#A two-sample t-test was conducted to compare the average number of fatalities in airplane crashes between the United States and Europe. 
# The results showed a statistically significant difference between the two regions (t = -3.37, p = 0.0008). 
# This suggests that the average number of fatalities per crash differs significantly between these regions.


sns.histplot(data=df, x='Fatalities', hue='Region', bins=30)
plt.show()

#Crash frequency has decreased in recent decades, suggesting improvements in aviation safety.
#A statistically significant difference in fatalities exists between the United States and Europe, possibly reflecting differences in aircraft types, routes, or operational conditions.
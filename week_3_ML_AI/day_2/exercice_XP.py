import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',None)

# Tip: The recommended preprocessing sequence is:
# 1. Handle duplicates
# 2. Address missing values
# 3. Treat outliers
# 4. Encode categorical variables

df = pd.read_csv('/Users/mariekrammer/Desktop/DI learning/week_3_ML_AI/day_1/datasets_for_exercises/titanic (1)/train.csv')
#print(df.head())
print(df.shape)

# 1. Handle duplicates
print(df[df.duplicated()])
df = df.drop_duplicates()
#print(df_no_dup.head())
print(df.shape)

# 2. Address missing values

#df_no_dup.info()
# missing values in age column (177), cabin column(687) and embarked column (2)
df = df.drop(columns=['Cabin'])
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)
df = df.dropna()
#df.info()


#Exercise 3
df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
df['Family Size'] = df['Parch'] + df['SibSp'] + 1
#df['Sex']=df['Sex'].map({'male':0, 'female':1})
#print(df['Embarked'].value_counts())
df = pd.get_dummies(df, columns=['Title','Embarked','Sex'])

print(df.head())

#3. Treat outliers
#Exercise 4
#sns.histplot(data = df, x='Fare')
#sns.boxplot(data=df,x='Fare',palette='Set2'  # Nice color palette)

#plt.show()

#sns.boxplot(data=df,x='Family Size',palette='Set2'  # Nice color palette)
#plt.show()


#sns.boxplot(data=df,x='Age',palette='Set2')  # Nice color palette))
#plt.show()

#capping
lower = df['Fare'].quantile(0.01)
upper = df['Fare'].quantile(0.99)

df['Fare'] = df['Fare'].clip(lower, upper) 


lower_age = df['Age'].quantile(0.05)
upper_age = df['Age'].quantile(0.95)

df['Age'] = df['Age'].clip(lower_age, upper_age) 

#Exercise5

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

scaler = MinMaxScaler()
df['Fare_normalized'] = scaler.fit_transform(df[['Fare']])

#print(df['Age'].skew())

scaler = StandardScaler()
df[['Family Size']] = scaler.fit_transform(df[['Family Size']])
df['Age_normalized'] = scaler.fit_transform(df[['Age']])


#exercise 6
print(df.columns)

df['Age_group']=pd.cut(df['Age'],bins=[0, 12, 18, 60, 100],labels=['child', 'teen', 'adult', 'senior'])
df = pd.get_dummies(df, columns=['Age_group'])

print(df.select_dtypes(include=['int64','float64']))
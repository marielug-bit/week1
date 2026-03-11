from exercice_XP import df

import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
pd.set_option('display.max_columns',None)

from sklearn.preprocessing import MinMaxScaler #distribution age
from sklearn.preprocessing import StandardScaler #distribution gaussienne

#identifier les colonnes numeriques du df
print(df.select_dtypes(include=['int64','float64']))

#sns.histplot(data = df, x='Pclass')
#plt.show()

scaler = MinMaxScaler()
df['SibSp_normalized']=scaler.fit_transform(df[['SibSp']])
df['Parch_normalized']=scaler.fit_transform(df[['Parch']])
df['Pclass_normalized']=scaler.fit_transform(df[['Pclass']])

from sklearn.model_selection import train_test_split

X = df.drop(columns=['Survived','Name','Ticket'])
y = df['Survived']

#from sklearn.linear_model import LogisticRegression
#model = LogisticRegression()

#model.fit(X, y)

#X_test = pd.read_csv('/Users/mariekrammer/Desktop/DI learning/week_3_ML_AI/day_1/datasets_for_exercises/titanic (1)/test.csv') 
#pred = model.predict(X_test)

sns.histplot(data = df, x='Age')
plt.show()

df = df.drop(columns=['Name','Ticket','Fare','Age','SibSp','Parch','Pclass'])
print(df.head())
from sklearn.decomposition import PCA

#This line creates an instance of the PCA class with the parameter n_components set to 2. It specifies that we want to reduce the dimensionality of the data to 2 principal components. In other words, the data will be projected into a 2D space.
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(df)

agg_data = df.groupby(df['Pclass_normalized'])[["Age_normalized", "Fare_normalized"]].mean()

print(agg_data)


df2 = pd.read_csv('/Users/mariekrammer/Desktop/DI learning/week_3_ML_AI/day_2/superstore_dataset2011-2015.csv')
df2.head()
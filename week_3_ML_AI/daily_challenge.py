import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
import xlrd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

df = pd.read_excel('/Users/mariekrammer/Desktop/DI learning/week_3_ML_AI/day_5_mini_project/US Superstore data.xls', engine='xlrd')

#Data visualization with matplotlib
#Create an interactive line chart to show sales trends over the years.
#Build an interactive map to visualize sales distribution by country.

print(df.head())
print(df.shape) # (9994, 21)
print(df.info()) # no missing values
print(df.describe())

df['Year of Order'] = df['Order Date'].dt.year
df_year = df.groupby('Year of Order')['Sales'].sum().reset_index()


plt.figure(figsize=(10,6))

sns.lineplot(data=df_year, x='Year of Order', y='Sales', marker='o')

plt.title('Sales variation over years')
plt.xlabel('Years')
plt.ylabel('Sales')

plt.grid()
plt.show()

df_state = df.groupby('State')['Sales'].sum().reset_index()
df_state = df_state.sort_values(by='Sales', ascending=False).head(10)

plt.figure(figsize=(12,6))

sns.barplot(data=df_state, x='State', y='Sales')

plt.title('Top 10 States by Sales')
plt.xlabel('State')
plt.ylabel('Sales')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Data Visualization with Seaborn:
#Use Seaborn to generate a bar chart showing top 10 products by sales.
#Create a scatter plot to analyze the relationship between profit and discount.

df_product = df.groupby('Product Name')['Sales'].sum().reset_index()
df_product =df_product.head(10)
plt.figure(figsize=(14,6))
sns.barplot(data = df_product, y='Product Name',x='Sales')
plt.title('top 10 products')
plt.xlabel('Products')
plt.ylabel('sales')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()


#Create a scatter plot to analyze the relationship between profit and discount.
sns.lineplot(data=df, x='Profit', y='Discount')
plt.title('Profit VS Discount')
plt.xlabel('Profit')
plt.ylabel('Discount')
plt.tight_layout()
plt.show()



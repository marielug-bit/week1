import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
import xlrd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

df = pd.read_excel('/Users/mariekrammer/Desktop/DI learning/week_3_ML_AI/day_5_mini_project/US Superstore data.xls', engine='xlrd')

print(df.head())
print(df.shape) # (9994, 21)
print(df.info()) # no missing values
print(df.describe())


# No duplicates
#print(df[df.duplicated()])

#print(df['Segment'].unique())
#print(df[df['Segment']=='Corporate'].head())

#Outliers


#Feature enginering
df['Profit_Margin'] = df['Profit'] / df['Sales'] # si c est superieur a 0 c est rentable sinon nan
df['Discount_Impact'] = (df['Sales'] / (1 - df['Discount'])) - df['Sales']
df['Month of ORDER'] = df['Order Date'].dt.month
df['Year of Order'] = df['Order Date'].dt.year
df['Month_Year'] = df['Order Date'].dt.to_period('M')

print(df.describe())

#Outliers
print(df[df['Discount_Impact']==22638.480000])

#cols = ['']

#df.hist()
#plt.tight_layout()
#plt.show()


print(df.groupby('State')['Sales'].sum().reset_index())

state_sales = df.groupby('State')['Sales'].sum().reset_index()
state_sales = state_sales.sort_values('Sales',ascending=False)
top10 = state_sales.head(15)
other = state_sales['Sales'].sum() - state_sales['Sales'].head(15).sum()
state_sales = state_sales.head(15)
state_sales['Other'] = other

# add an other row
other_row = pd.DataFrame({
    'State': ['Other'],
    'Sales': [other]
})

state_sales=pd.concat([state_sales, other_row], ignore_index=True)


sns.barplot(data = state_sales,x='State',y='Sales',palette='coolwarm')
plt.xticks(rotation=45,ha = 'right')
plt.title('Sales per State')
plt.xlabel('State')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

#Which states have the most sales? California, New York, Texas, Washington, Pensylvania, Florida


#What is the difference between New York and California in terms of sales and profit? 
#(Compare the total sales and profit between New York and California.)

state_sales_and_profit = df.groupby('State')[['Sales','Profit']].sum().reset_index()
#state_profit = df.groupby('State')['Profit'].sum().reset_index()
California_NY_data = state_sales_and_profit.loc[(state_sales_and_profit['State']=='California')|(state_sales_and_profit['State']=='New York'),['State','Sales','Profit']]
print(California_NY_data.head())
sns.scatterplot(data = California_NY_data,x='Sales',y='Profit',hue = 'State')
plt.show()

#California has more sales and profit than NY

#Who is an outstanding customer in New York?
#print(df.loc[(df['State']=='New York')].groupby('Customer Name').head())
NY_customers = df[df['State']=='New York'].groupby('Customer Name')[['Sales','Profit']].sum().sort_values('Sales', ascending=False)
print(NY_customers.head(10))
sns.scatterplot(data = NY_customers.head(10),x='Sales',y='Profit',hue = 'Customer Name')
plt.title('10 best customer')
plt.show()
# the answer is Tom Ashbrook 

#Are there any differences among states in profitability?
#state_profit = df.groupby('State')[['Profit']].sum().reset_index()
grouped = df.groupby('State')
groups = []
for state,group in grouped: #state est le nom du group, group est un mini dataframe contenant seulement ce groupe
    groups.append(group['Profit'].values) # values permet de faire une un tableau numpy de profits pour chaque etat, on ajoute dans une liste

f_value,p_value = stats.f_oneway(*groups)

print('F-value: ', f_value)
print('P-value: ',p_value)

if p_value < 0.05:
    print("There are significant differences in profitability between states.")
else:
    print("No significant differences in profitability between states.")

#there is a significant difference in profitability between states

#The Pareto Principle, also known as the 80/20 rule, is a concept derived from the work of Italian economist 
# Vilfredo Pareto. It states that roughly 80% of the effects come from 20% of the causes. For instance, 
# identifying the top 20% of products that generate 80% of sales or the top 20% of customers that contribute 
# to 80% of profit can help in prioritizing efforts and resources. This focus can lead to improved 
# efficiency and effectiveness in business strategies. Can we apply Pareto principle to customers and Profit ?
#  (Determine if 20% of the customers contribute to 80% of the profit.)

df_customer = df.groupby('Customer Name')[['Sales','Profit']].sum().reset_index()
df_profit = df_customer.sort_values('Profit',ascending = False)



df_profit = df_profit.head(int(round(len(df_customer)*20/100)))

customers = ['the first 20% of customers','Other 80%']
profits = [(df_profit['Profit'].sum()), (df['Profit'].sum()-df_profit['Profit'].sum())]

plt.bar(customers,profits)
plt.title('20 VS the rest of customers')
plt.xlabel('customers')
plt.ylabel('profit')
plt.show()

print(df_profit['Profit'].sum())
print(df['Profit'].sum()*80/100)
if df_profit['Profit'].sum() >= ((df['Profit'].sum())*80)/100:
    print('we can apply Pareto principle to customers and Profit')
else:
    print('we can not apply Pareto principle to customers and Profit')



#What are the Top 20 cities by Sales ? What about the Top 20 cities by Profit ? Are there any difference 
# among cities in profitability ? (Identify the top 20 cities based on total sales and total profit 
# and analyze differences in profitability among these cities.)

fig, axes = plt.subplots(1,2,figsize=(14,5))


df_top_cities = df.groupby('City')['Sales'].sum().reset_index()
df_top_cities = df_top_cities.sort_values('Sales',ascending=False)
df_top_20_cities = df_top_cities.head(20)

df_top_cities_profit = df.groupby('City')['Profit'].sum().reset_index()
df_top_cities_profit = df_top_cities_profit.sort_values('Profit',ascending=False)
df_top_20_cities_profit = df_top_cities_profit.head(20)



sns.barplot(ax=axes[0],data = df_top_20_cities, x='City',y='Sales')
axes[0].set_title('best 20 cities for sales')
axes[0].set_xlabel('cities')
axes[0].set_ylabel('sales')
axes[0].tick_params(axis='x', rotation=45)


sns.barplot(ax=axes[1],data = df_top_20_cities_profit, x='City',y='Profit')
axes[1].set_title('best 20 cities for profit')
axes[1].set_xlabel('cities')
axes[1].set_ylabel('profit')
axes[1].tick_params(axis='x', rotation=45)


plt.tight_layout()
plt.show()

#there any difference among cities in profitability, first ones : NY, Seatle, san franscisco

grouped_profit = df.groupby('City')
groups_profit = []
for state,group in grouped_profit: #state est le nom du group, group est un mini dataframe contenant seulement ce groupe
    groups_profit.append(group['Profit'].values) # values permet de faire une un tableau numpy de profits pour chaque etat, on ajoute dans une liste

f_value,p_value = stats.f_oneway(*groups)

print('F-value of profit: ', f_value)
print('P-value of profit: ',p_value)

if p_value < 0.05:
    print("There are significant differences in profit in profitability between cities.")
else:
    print("No significant differences in profit in profitability between cities.")



grouped_sales = df.groupby('City')
groups_sales = []
for state,group in grouped_sales: #state est le nom du group, group est un mini dataframe contenant seulement ce groupe
    groups_sales.append(group['Sales'].values) # values permet de faire une un tableau numpy de profits pour chaque etat, on ajoute dans une liste

f_value,p_value = stats.f_oneway(*groups)

print('F-value of sales: ', f_value)
print('P-value of sales: ',p_value)

if p_value < 0.05:
    print("There are significant differences in sales in profitability between cities.")
else:
    print("No significant differences in sales in profitability between cities.")

#What are the Top 20 customers by Sales?
df_customer = df.groupby('Customer Name')[['Sales']].sum().reset_index()
df_customer = df_customer.sort_values('Sales',ascending=False)
df_customer = df_customer.head(20)


sns.barplot(data = df_customer, x='Customer Name', y = 'Sales',palette ='viridis')
plt.title('TOP 20 customers')
plt.xlabel('Customers')
plt.ylabel('Sales')
plt.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()

df_customer['cumulative_sales'] = df_customer['Sales'].cumsum()
df_customer['cumulative_percent'] = 100 * df_customer['cumulative_sales'] / df_customer['Sales'].sum()

plt.figure(figsize=(10,6))

plt.plot(df_customer['cumulative_percent'], marker='o')

plt.axhline(80, color='red', linestyle='--')  # ligne 80%
plt.title('Cumulative Sales by Customers')
plt.xlabel('Customers (sorted)')
plt.ylabel('Cumulative % of Sales')

plt.grid()
plt.show()

pareto_cutoff = df_customer[df_customer['cumulative_percent'] <= 80]
print("Number of customers for 80% sales:", len(pareto_cutoff))
print("Total customers:", len(df_customer))

#The Pareto principle applies: a small proportion of customers generates the majority of sales.

#Based on the analysis, make decisions on which states and cities to prioritize for marketing strategies.
#states to prioritize: California, NY, Whashington,Texas
#cities to prioritize:NY, LA, Seatle, San fransisco,Detroit

df_customer = df.groupby('Customer Name').agg({
    'Sales': 'sum',
    'City': 'first',
    'State': 'first'
}).reset_index()

print(df_customer.sort_values('Sales',ascending = False).head(20))
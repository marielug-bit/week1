
import pandas as pd
# 🌟 Exercise 1: Understanding Data Visualization
# Task: Explain why data visualization is important in data analysis.
# Task: Describe the purpose of a line graph in data visualization.
# Exercise 1: Understanding Data Visualization

# Data visualization is important in data analysis because it helps transform raw data
# into visual formats such as charts and graphs. This makes the data easier to understand,
# interpret, and communicate.

# Visualizations allow analysts to quickly identify patterns, trends, relationships,
# and anomalies that might be difficult to detect by looking only at numerical tables.

# For example, a line graph can show how a variable changes over time, making it easy
# to see increases, decreases, or seasonal patterns.

# The purpose of a line graph is to represent the relationship between variables,
# usually over time. It connects data points with lines to highlight trends and
# changes in the data.


# 🌟 Exercise 2: Creating a Line Plot for Temperature Variation
# Objective: Create a simple line plot using Matplotlib that represents temperature variations over a week.

# Tasks:
# - Use a list of temperature values for each day of the week
#   (e.g., [72, 74, 76, 80, 82, 78, 75]).
# - Label the x-axis as “Day”.
# - Label the y-axis as “Temperature (°F)”.
# - Add a title to the plot.
# - Display the plot.

import matplotlib.pyplot as plt

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
temperatures = [72, 74, 76, 80, 82, 78, 75]

plt.plot(days,temperatures,marker='o',linewidth=2,markersize=8,color = 'steelblue')
plt.title('Temperature Variation Over a Week', fontsize=16, fontweight='bold')
plt.xlabel('Day', fontsize=12)
plt.ylabel('Temperature (F)', fontsize=12)
plt.grid(True, alpha=0.3)  # Subtle gridlines
plt.ylim(min(temperatures)-3, max(temperatures)+3)  # Set Y-axis range to emphasize variation

plt.show()


# 🌟 Exercise 3: Visualizing Monthly Sales with a Bar Chart
# Objective: Generate a bar chart using Matplotlib to visualize monthly sales data for a retail store.

# Tasks:
# - Create a list of sales values for each month
#   (e.g., [5000, 5500, 6200, 7000, 7500]).
# - Label the x-axis as “Month”.
# - Label the y-axis as “Sales Amount ($)”.
# - Add a title to the bar chart.
# - Display the plot.

months = ['January', 'February', 'March', 'April', 'May']
sales = [5000, 5500, 6200, 7000, 7500]

plt.figure(figsize=(10, 6))

bars = plt.bar(months, sales,
               color='coral',         # Nice color
               edgecolor='black',     # Border around bars
               linewidth=1.2)

plt.title('Monthly Sales Report', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales Amount ($)', fontsize=12)
plt.xticks(rotation=45, ha='right')  # Rotate labels if needed

# Add value labels on top of each bar
for bar, value in zip(bars, sales):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100,
             f'${value:,}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()  # Prevent labels from being cut off
plt.show()


# 🌟 Exercise 4: Visualizing the Distribution of CGPA
# Objective: Create a histogram to visualize the distribution of students’ CGPA.

# Dataset Overview:
# Assume the CGPA data is categorized into ranges and loaded in a DataFrame named df.

# Tasks:
# - Import necessary libraries.
# - Use Seaborn’s histplot to create a histogram of the CGPA categories.
# - Customize the histogram with a specific color and add a title.
# - Display the plot.

df_mental_health = pd.read_csv('/Users/mariekrammer/Desktop/DI learning/week_3_ML_AI/day_4/Student Mental health.csv')
import seaborn as sns
print(df_mental_health.head())

#print(df_mental_health['What is your CGPA?'].describe())
plt.figure(figsize=(10,6))
sns.histplot(data = df_mental_health, x='What is your CGPA?',bins=6,color='steelblue')
plt.title('CGPA',fontsize=16,fontweight='bold')
plt.xlabel('CGPA',fontsize=12)
plt.ylabel('Frequency',fontsize=12)
plt.show()

# 🌟 Exercise 5: Comparing Anxiety Levels Across Different Genders
# Objective: Use a bar plot to compare the proportion of students experiencing anxiety across different genders.

# Dataset Overview:
# The dataset includes the columns: 'Do you have Anxiety?' and 'Choose your gender'.

# Tasks:
# - Import the necessary libraries.
# - Use Seaborn to create a bar plot comparing anxiety levels across genders from the dataset df.
# - Customize the plot with an appropriate color palette and add a title.
# - Display the plot.

#print(df_mental_health['Do you have Anxiety?'].unique())
plt.figure(figsize=(10,6))
sns.countplot(data = df_mental_health,x='Choose your gender',hue='Do you have Anxiety?',palette = 'viridis')
plt.title('Anxiety levels across genders', fontsize = 14)
plt.xlabel('Genre',fontsize = 12)
plt.ylabel('Anxiety',fontsize = 12)
plt.show()

# 🌟 Exercise 6: Exploring the Relationship Between Age and Panic Attacks
# Objective: Create a scatter plot to explore the relationship between students’ age
# and the occurrence of panic attacks.

# Dataset Overview:
# The dataset includes the columns: 'Age' and 'Do you have Panic Attacks?'.

# Tasks:
# - Import the necessary libraries.
# - Convert panic attack responses to numeric values (e.g., Yes = 1, No = 0).
# - Use Seaborn’s scatterplot to create a scatter plot with 'Age' on the x-axis
#   and the numeric panic attack responses on the y-axis.
# - Customize the plot to improve readability by adding labels, a title,
#   and adjusting point styles.
# - Display the plot.
print(df_mental_health.columns)
print(df_mental_health['Do you have Panic attack?'].unique())
df_mental_health['Panic_Attacks'] = df_mental_health['Do you have Panic attack?'].map({'Yes':1,'No':0})
plt.figure(figsize=(10,6))
sns.scatterplot(data=df_mental_health,x='Age',y='Panic_Attacks',alpha=0.6)
plt.title('Panic Attack VS Age')
plt.xlabel('Age',fontsize = 12)
plt.ylabel('Panic Attacks',fontsize = 12)
plt.show()


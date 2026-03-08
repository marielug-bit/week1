#Exercise 1
# Data analysis is the science of collecting, processing, and interpreting data
# in order to make decisions or better understand the world around us.
#
# It has become essential today because it affects almost every area of life
# and because billions of pieces of information are generated every day.
#
# Today, data analysis is used in many fields:
# - in the medical field, to detect diseases or study epidemics
# - in the financial sector, to analyze markets and predict trends
# - in social media, to understand user behavior and improve services
#
# Therefore, data analysis plays a key role in decision-making
# and innovation across many industries.

#Exercise 2
#on jupiter note book

#exercise 3
import pandas as pd
pd.set_option('display.max_columns',None)
df1 = pd.read_csv('/Users/mariekrammer/Desktop/DI learning/week_3_ML_AI/day_1/Mental health Depression disorder Data.csv')
#print(df1.head())
#print(df1.columns)
#qualitative, nominal = index(maybe ordered?), entity,Code
#quantitative, discrete = year
# quantitative, discrete = everything else

df2 =pd.read_csv('/Users/mariekrammer/Desktop/DI learning/week_3_ML_AI/day_1/Time Americans Spend Sleeping.csv')
print(df2.head())
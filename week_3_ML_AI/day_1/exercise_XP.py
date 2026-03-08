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
# quantitative, continuous = everything else

df2 =pd.read_csv('/Users/mariekrammer/Desktop/DI learning/week_3_ML_AI/day_1/Time Americans Spend Sleeping.csv')
print(df2.head())
#qualitative, nominal = index, Period,type of days,activity,sex,age group
#quantitative, discrete = year
# quantitative, continuous = avg hours per day sleeping,standard error

#exercise 4 on jupyter notebook

#exercise 6
#A company’s financial reports stored in an Excel file. structured data
#Photographs uploaded to a social media platform. unstructured data
#A collection of news articles on a website.unstructured data
#Inventory data in a relational database.structured data
#Recorded interviews from a market research study.unstructured data

#exercise 7
#A series of blog posts about travel experiences. text analysis, excel file with the destination, activity, language, budget,satisfaction
#Audio recordings of customer service calls. class them according to the customer's demand
# Handwritten notes from a brainstorming session. OCR, group according to the category, priority
#tutorial : speech to text, structure according to ingredients, steps..

import pandas as pd
url = 'https://raw.githubusercontent.com/marielug-bit/week1/main/week_3_ML_AI/day_1/train.csv'
df = pd.read_csv(url)
print(df.head())

data = {
    'Name' : ['Marie','David','Yehuda'],
    'Age': [27,28,1]
}
df = pd.DataFrame(data)
print(df)

df.to_excel("data.xlsx", index=False)
df.to_json("data.json")
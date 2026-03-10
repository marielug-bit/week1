import kagglehub
import pandas as pd
pd.set_option('display.max_columns',None)
import os

# Download latest version
path = kagglehub.dataset_download("altavish/boston-housing-dataset")

#print("Path to dataset files:", path)

#print(os.listdir(path))
#file_path = os.path.join(path, "HousingData.csv")
#df = pd.read_csv(file_path)
#print(df.head())
#print(df.describe())

#Exercise 3
#df3 = pd.read_csv('/Users/mariekrammer/Desktop/DI learning/week_3_ML_AI/day_1/datasets_for_exercises/data.csv',encoding="latin-1")
#print(df3.head())
#print(df3.shape)
#print(df3.columns)
#structured data = tout sauf la description
#la description est semi structuree
#reviewsn, longevite?, descriptif du produit, image du produit,social media posts
#analyser la satisfactio des clients, comprendre pourquoi certains produits se vendent mieux ou tres souvent, sentiment analysis sur les commentaires, ameliorer les recommendations de produits

#Exercise4
#df4 = pd.read_csv('/Users/mariekrammer/Desktop/DI learning/week_3_ML_AI/day_1/datasets_for_exercises/Metro_Interstate_Traffic_Volume.csv')
#print(df4.head())
#print(df4.shape)
#ca dit la meteo toute les heures du 2 fevrier 2012 au 2018-09-30, soit plus de 2008 jours, soit 5 ans et demie.
#print(df4.iloc[48203])
#print(df4.tail(1))
#print(df4[df4['holiday'].notna()])
#structure = temp,rain,snow.clouids_all,date_time,trafic_volume, holiday, weather_main
#unstructured = weather_description

#Exercise5
#c est bon

#Exercise6
from faker import Faker
fake = Faker()
import random
products = []

for i in range(500):
    product = {
        "product_id": i + 1,
        "name": fake.word().capitalize(),
        "description": fake.sentence(),
        "price": round(random.uniform(5, 500), 2)
    }
    
    products.append(product)

df_products = pd.DataFrame(products)
print(df_products.head())
print(df_products.shape)
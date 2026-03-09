import kagglehub
import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("altavish/boston-housing-dataset")

print("Path to dataset files:", path)

print(os.listdir(path))
file_path = os.path.join(path, "HousingData.csv")
df = pd.read_csv(file_path)
print(df.head())
print(df.describe())
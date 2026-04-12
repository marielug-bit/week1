# Data Exploration : Load and visualize the data
# Use pandas to load the dataset and examine the first few rows.
# Create a scatter plot to visualize the data points for students who were admitted versus those 
# who were not based on their exam scores.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay


df = pd.read_csv('ex2data1.txt',header = None)

print(df.head())
print(df.info())
print(df.columns)
df.columns = ['exam1', 'exam2', 'admitted']

plt.scatter(df['exam1'], df['exam2'], c=df['admitted'])
plt.title(f'Admissions')
plt.xlabel('Exam1')
plt.ylabel('Exam2')

plt.show()


# Applying Logistic Regression with scikit-learn:

# Implement logistic regression using the LogisticRegression function from scikit-learn to find the best parameters for your model.
# Train the logistic regression model on your dataset.
X = df.drop(columns=['admitted'])
y = df['admitted']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,stratify=y)

model = LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)


# Making Predictions:

# Use the trained logistic regression model to make predictions on your dataset.
# Calculate the accuracy of your model.

y_pred = model.predict(X_test)

acc = accuracy_score(y_test,y_pred)
prec = precision_score(y_test,y_pred)
rec = recall_score(y_test,y_pred)
f1 = f1_score(y_test,y_pred)

print("Accuracy:", round(acc,4))
print("Precision:", round(prec,4))
print("Recall:", round(rec,4))
print('F1:', round(f1,4))

# Simple bar plot of metrics
import matplotlib.pyplot as plt
plt.figure()
plt.bar(['accuracy','precision','recall','f1'], [acc,prec,rec,f1])
plt.title('Metrics on test')
plt.ylabel('Score')
plt.show()

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(cm)
disp.plot()
plt.title('Confusion matrix')
plt.show()

# 
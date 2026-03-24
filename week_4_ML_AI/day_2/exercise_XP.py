# 🌟 Exercise 1 : Matrix Operations
# Instructions
# In this exercise, you’ll work with a 3x3 matrix. Here’s a brief explanation of the concepts:

# Determinant: The determinant is a value that can be computed from the elements of a square matrix.
# It provides important information about the matrix, such as whether it has an inverse, and is used 
# in various areas like linear algebra and calculus. To understand more about it you can watch this video.
# Inverse of a Matrix: The inverse of a matrix is a matrix that, when multiplied with the original matrix,
# results in an identity matrix. Not all matrices have inverses. The inverse is crucial in solving systems 
# of linear equations.

# Create a 3x3 matrix and perform the following operations:
import numpy as np
A = np.random.uniform(1,10,(3,3))
print(A)


# Calculate the determinant.
det = np.linalg.det(A)
print(det)
# Find the inverse of the matrix.
if det:
    B = np.linalg.inv(A)
    print(B)




# 🌟 Exercise 2 : Statistical Analysis
# Instructions
# In this exercise, you’ll calculate statistical measures for a dataset:

# Mean: The average value of a dataset.
# Median: The middle value in a dataset when it is arranged in ascending or descending order.
# Standard Deviation: A measure of the amount of variation or dispersion in a set of values.

# Using NumPy, generate an array of 50 random numbers and compute:
arr = np.random.uniform(1,50,50)
# The mean and median.
mean = np.mean(arr)
med = np.median(arr)
print(f'Mean of the array is {mean} \nMedian of array is {med}')
# The standard deviation.
std = np.std(arr)
print(f'standard deviation of the array is {std}') 

# 🌟 Exercise 3 : Date Manipulation
# Instructions
# Create a NumPy array of dates for the month of January 2023. Convert these dates to another format 
# (e.g., YYYY/MM/DD).

january = np.arange('2023-01-01','2023-02-01',dtype='datetime64[D]')
#print(january)
january_string = january.astype(str)
formated = np.char.replace(january_string, '-', '/')
#print(formated)

# 🌟 Exercise 4 : Data Manipulation with NumPy and Pandas
# Instructions
# Create a DataFrame with random numbers and perform:
import pandas as pd
df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])
print(df)
# Conditional selection of data.
high = df[df>0.5]
print(high)
# Aggregation functions like sum and average.
mean = np.mean(df)
sum = np.sum(df)
print(mean, sum)


# 🌟 Exercise 5 : Image Representation
# Instructions
# Explain how images are represented in NumPy arrays and demonstrate with a simple example 
# (e.g., creating a 5x5 grayscale image).
# an image is lique a 3D matrix where each value depicts a pixel in the image

image = np.array([
    [0, 50, 100, 150, 200],
    [10, 60, 110, 160, 210],
    [20, 70, 120, 170, 220],
    [30, 80, 130, 180, 230],
    [40, 90, 140, 190, 255]
])

import matplotlib.pyplot as plt

plt.imshow(image, cmap='gray')
plt.show()



# 🌟 Exercise 6 : Basic Hypothesis Testing
# Instructions
# Create a sample dataset to test the effectiveness of a new training program on employee productivity:

# Productivity scores of employees before the training program
productivity_before = np.random.normal(loc=50, scale=10, size=30)

# Productivity scores of the same employees after the training program
productivity_after = productivity_before + np.random.normal(loc=5, scale=3, size=30)

# Your task is to formulate a hypothesis regarding the training program's effectiveness 
# and test it using basic statistical functions in NumPy.
#Null_hypothesis = there is no difference before and after the training

mean_before = np.mean(productivity_before)
mean_after = np.mean(productivity_after)

print("Before:", mean_before)
print("After:", mean_after)

if mean_after > mean_before:
    print("The training program improved productivity")
else:
    print("No improvement detected")


# 🌟 Exercise 7 : Complex Array Comparison
# Instructions
# Create two arrays and perform element-wise comparison to find which elements are greater in the first array.

# The expected output is a boolean array showing which elements in the first array are greater than 
# the corresponding elements in the second array.

first_arr = np.random.uniform(1,50,10)
second_arr = np.random.uniform(1,50,10)
higher = np.where(first_arr>second_arr,True,False)
print(higher)

# 🌟 Exercise 8 : Time Series Data Manipulation
# Instructions
# Generate time series data for the year 2023. Demonstrate slicing for the following intervals:
year_2023 = np.arange('2023-01-01', '2024-01-01', dtype='datetime64[D]')
# January to March
# April to June
# July to September
# October to December
quarters = [
    ("Q1: Jan-Mar", '2023-01-01', '2023-04-01'),
    ("Q2: Apr-Jun", '2023-04-01', '2023-07-01'),
    ("Q3: Jul-Sep", '2023-07-01', '2023-10-01'),
    ("Q4: Oct-Dec", '2023-10-01', '2024-01-01'),
]

for name, start, end in quarters:
    mask = year_2023[(year_2023 >= np.datetime64(start)) & (year_2023 < np.datetime64(end))]  # boolean mask: dates >= start AND dates < end
    print(f"{name} is composed of {mask}")
# Generate a time series data for a specific period and demonstrate how to slice this data for different intervals.


#🌟 Exercise 9 : Data Conversion
#Instructions
#Demonstrate how to convert a NumPy array to a Pandas DataFrame and vice versa.
arr = np.array([[1,2,3],[4,5,6]])
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df)

df_to_numpy = df.to_numpy()

# 🌟 Exercise 10 : Basic Visualization
# Instructions
# Use Matplotlib to visualize a simple dataset created with NumPy (e.g., a line graph of random numbers).


import matplotlib.pyplot as plt

# Plotting with NumPy arrays
plt.scatter(df['A'],df['B'])
plt.title("df Scatter Plot")
plt.xlabel("A")
plt.ylabel("value")
plt.show()


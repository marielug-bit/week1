# Exercise 1
#Create a 1D NumPy array containing numbers from 0 to 9.

import numpy as np
arr = np.arange(10)
print(arr)

#Exerise 2
#Convert a list [3.14, 2.17, 0, 1, 2] into a NumPy 
# array and convert its data type to integer.

float_arr = np.array([3.14, 2.17, 0, 1, 2])
int_arr = float_arr.astype(int)
print(int_arr)

#Exercise 3
#Create a 3x3 NumPy array with values ranging from 1 to 9.
arr_1_to_9 = np.arange(1,10).reshape((3,3))
print(arr_1_to_9)

#exercise4
#Create a 2D NumPy array of shape (4, 5) filled with random numbers.
arr_random = np.random.random((4, 5))
print(arr_random)

#exercise5
array = np.array([[21,22,23,22,22],[20, 21, 22, 23, 24],[21,22,23,22,22]])
second_row = array[1,:]
print(second_row)

#Exercise 6 : Reversing elements
#Reverse the order of elements in a given 1D NumPy array (first element becomes last).
array_to_reverse = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
reversed_array = array_to_reverse[::-1]
print(reversed_array)

# Exercise 7 : Identity Matrix
identify_4 = np.eye(4)
print(identify_4)

#Exercise 8 : Simple Aggregate Funcs
print(f'Sum: {array_to_reverse.sum()}  Average: {array_to_reverse.mean()}')

#Exerise. 9
#Create a NumPy array with elements from 1 to 20; then reshape it into a 4x5 matrix.
arr_1_to_20 = np.arange(1,21)
arr_final = arr_1_to_20.reshape((4,5))

# Exercise 10 : Conditional Selection of Values
#Extract all odd numbers from a given NumPy array.
print(arr_1_to_9[arr_1_to_9%2==1])

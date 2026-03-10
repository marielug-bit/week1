# ==================================================
# 🧠 What You Will Learn
# ==================================================
# - Conditionals (if / else)
# - Loops (for / while)
# - Functions
#


# ==================================================
# Exercise 1
# ==================================================
# Instructions:
# Write a script that inserts an item at a defined index in a list.

lst = [1,2,3]
lst.insert(1,7)
print(lst)

# ==================================================
# Exercise 2
# ==================================================
# Instructions:
# Write a script that counts the number of spaces in a string.
#
str = 'a little princess'
print(str.count(' '))

# ==================================================
# Exercise 3
# ==================================================
# Instructions:
# Write a script that calculates the number of upper case
# letters and lower case letters in a string.
#
count1 = 0
count2 = 0
for char in str:
    if char.isalpha():
        if char.islower():
            count1 += 1
        else:
            count2 += 1
num_lowercase_letters = count1
num_uppercase_letters = count2

# ==================================================
# Exercise 4
# ==================================================
# Instructions:
# Write a function to find the sum of an array
# WITHOUT using the built-in sum() function.
#
# Example:
# my_sum([1,5,4,2])
# Output: 12
#
def my_sum(lst):
    count = 0
    for item in lst:
        count+=item
    return count


# ==================================================
# Exercise 5
# ==================================================
# Instructions:
# Write a function to find the maximum number in a list.
#
# Example:
# find_max([0,1,3,50])
# Output: 50
def find_max(lst):
    current_max = lst[0]
    for value in lst[1:]:
        if value > current_max:
            current_max = value
    return current_max



# ==================================================
# Exercise 6
# ==================================================
# Instructions:
# Write a function that returns the factorial of a number.
#
# Example:
# factorial(4)
# Output: 24
#


# ==================================================
# Exercise 7
# ==================================================
# Instructions:
# Write a function that counts how many times an element
# appears in a list (WITHOUT using the .count() method).
#
# Example:
# list_count(['a','a','t','o'],'a')
# Output: 2
#


# ==================================================
# Exercise 8
# ==================================================
# Instructions:
# Write a function that returns the L2-norm
# (square root of the sum of squares) of a list.
#
# Example:
# norm([1,2,2])
# Output: 3
#


# ==================================================
# Exercise 9
# ==================================================
# Instructions:
# Write a function to check if a list is monotonic
# (sorted either ascending or descending).
#
# Examples:
# is_mono([7,6,5,5,2,0]) -> True
# is_mono([2,3,3,3]) -> True
# is_mono([1,2,0,4]) -> False
#


# ==================================================
# Exercise 10
# ==================================================
# Instructions:
# Write a function that prints the longest word in a list.
#


# ==================================================
# Exercise 11
# ==================================================
# Instructions:
# Given a list of integers and strings,
# separate them into two different lists:
# - one list with all integers
# - one list with all strings
#


# ==================================================
# Exercise 12
# ==================================================
# Instructions:
# Write a function to check if a string is a palindrome.
#
# Examples:
# is_palindrome('radar') -> True
# is_palindrome('John') -> False
#


# ==================================================
# Exercise 13
# ==================================================
# Instructions:
# Write a function that returns the number of words
# in a sentence with length greater than k.
#
# Example:
# sentence = 'Do or do not there is no try'
# k = 2
# sum_over_k(sentence, k) -> 3
#


# ==================================================
# Exercise 14
# ==================================================
# Instructions:
# Write a function that returns the average value
# in a dictionary (assume values are numeric).
#
# Example:
# dict_avg({'a':1,'b':2,'c':8,'d':1})
# Output: 3
#


# ==================================================
# Exercise 15
# ==================================================
# Instructions:
# Write a function that returns the common divisors
# of two numbers.
#
# Example:
# common_div(10,20)
# Output: [2,5,10]
#


# ==================================================
# Exercise 16
# ==================================================
# Instructions:
# Write a function that tests if a number is prime.
#
# Example:
# is_prime(11) -> True
#


# ==================================================
# Exercise 17
# ==================================================
# Instructions:
# Write a function that prints elements of a list
# if both the index AND the value are even.
#
# Example:
# weird_print([1,2,2,3,4,5])
# Output: [2,4]
#


# ==================================================
# Exercise 18
# ==================================================
# Instructions:
# Write a function that accepts an undefined number
# of keyword arguments and returns the count of
# different types.
#
# Example:
# type_count(a=1,b='string',c=1.0,d=True,e=False)
# Output:
# int:1, str:1, float:1, bool:2
#


# ==================================================
# Exercise 19
# ==================================================
# Instructions:
# Write a function that mimics the built-in .split() method.
#
# By default:
# - split on whitespace
# But:
# - should accept a custom separator as argument.
#


# ==================================================
# Exercise 20
# ==================================================
# Instructions:
# Convert a string into password format
# by replacing all characters with '*'.
#
# Example:
# input: "mypassword"
# output: "**********"
#


# ==================================================
# 🌟 One Last Thing:
# Good luck!
# ==================================================

print(10/3)
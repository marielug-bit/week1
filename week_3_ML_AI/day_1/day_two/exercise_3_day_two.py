# ==================================================
# Exercise 1: Formula
# ==================================================
#
# Instructions:
# Write a program that calculates and prints a value according to this formula:
#
#     Q = Square root of [(2 * C * D) / H]
#
# Fixed values:
C = 50
H = 30
#
# Steps:
# 1. Ask the user for a comma-separated string of numbers.
#    Example input: 100,150,180

# 2. For each number provided by the user:
#    - Use it as D in the formula
#    - Compute Q
#
# 3. Print all results in one line, separated by commas.
#
# Example:
# Input: 100,150,180
# Output:
# 18,22,24
numbers = input('choose a comma-separated string of numbers: ')
lst = numbers.split(",")
lst_int = list(map(int, lst))
new_list = [((2*C*value)/H)**(1/2) for value in lst_int]
print(",".join(str(x) for x in new_list))

# ==================================================
# Exercise 2: List of integers
# ==================================================
#
# Instructions:
# Given a list of 10 integers to analyze. For example:
# [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
# [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
# [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
# [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
#
# Tasks:
# 1. Store the list of numbers in a variable.
def square(num):
    return(num**2)
def task_with_list(lst):
    print(" ".join(str(num) for num in lst))
    sorted_desc = sorted(lst, reverse=True)
    print(sorted_desc)
    print(sum(lst))
    ls = [lst[0],lst[-1]]
    print(ls)
    lst_greater_50 = [value for value in lst if value > 50 ]
    print(lst_greater_50)
    lst_smaller_10 = [value for value in lst if value < 10 ]
    lst_squarred = list(map(square,lst))
    print(lst_squarred)
    num_set = set(lst)
    simple_lst = list(num_set)
    print(simple_lst)

# 2. Print:
#    a) The list of numbers in a single line
#    b) The list sorted in descending order (largest to smallest)
#    c) The sum of all numbers
#
# 3. Create and print a list containing the first and last numbers.
#
# 4. Create and print a list of all numbers greater than 50.
#
# 5. Create and print a list of all numbers smaller than 10.
#
# 6. Create and print a list of all numbers squared
#    Example: [1, 2, 3] -> print "1 4 9"
#
# 7. Create and print the numbers without duplicates
#    - Also print how many numbers are in the new list
#
# 8. Print the average of all the numbers.
#
# 9. Print the largest number.
#
# 10. Print the smallest number.
#
# 11. Bonus:
#     Find the sum, average, largest, and smallest without using built-in functions.
#
# 12. Bonus:
#     Instead of using a pre-defined list, ask the user for 10 integers
#     between -100 and 100 (repeat input 10 times and store them in a list).
#
# 13. Bonus:
#     Instead of asking the user, generate 10 random integers between -100 and 100.
#
# 14. Bonus:
#     Instead of always generating 10 integers, make the amount random too!
#     Generate a random positive integer no smaller than 50 (this will be the amount).
#
# 15. Bonus:
#     Will the code still work when the number of random numbers is not equal to 10?
#     (Think about which parts assume there are exactly 10 numbers.)


# ==================================================
# Exercise 3: Working on a paragraph
# ==================================================
#
# Instructions:
# 1. Find an interesting paragraph of text online
#    (keep it appropriate for the class).
#
# 2. Paste the paragraph into your code and store it in a variable.
#
# 3. Analyze the paragraph and print a nicely formatted message with:
#    - How many characters it contains
#    - How many sentences it contains
#    - How many words it contains
#    - How many unique words it contains
my_text = """Aujourd’hui, le ciel au-dessus de Jérusalem est majoritairement dégagé.
Le soleil domine une grande partie de la journée.
Les températures sont douces et agréables.
La soirée sera plus fraîche."""

num_characters = len(my_text)
num_sentences = my_text.count(".")
num_words = my_text.count(' ') + my_text.count('\n')+1
my_text_list = my_text.split(' ') + my_text.split('\n')
my_text_set = set(my_text_list)
print(len(my_text_set))
#Bonus
# - How many non-whitespace characters it contains
# - The average number of words per sentence
# - The amount of non-unique words in the paragraph

non_whitespace = len([c for c in my_text if not c.isspace()])
print(non_whitespace)

# ==================================================
# Exercise 4: Frequency Of The Words
# ==================================================
#
# Instructions:
# Write a program that prints the frequency (count) of each word from the input.
#
# Example input:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
#
# Expected output:
# (Print each word and how many times it appears in the text.)

# Notes:
# - Decide how you want to handle punctuation (.,?!) and capitalization (Python vs python).
# - You can print the results in any clear format (one word per line is common).

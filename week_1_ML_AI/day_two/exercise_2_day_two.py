#Exercise 1: Concatenate lists
# -----------------------------------------
# Instructions:
# Write code that concatenates two lists together
# WITHOUT using the + sign.
#
# Write your code below:
def concatenate_lists(lst1,lst2):
    result = lst1.extend(lst2)
    print(result)


# =========================================
# Exercise 2: Range of numbers
# -----------------------------------------
# Instructions:
# Create a loop that goes from 1500 to 2500
# and prints all multiples of 5 and 7.
#
# Write your code below:
for i in range(1500,2501):
    if i%5 == 0 or i%7 == 0:
        print(i)

# =========================================
# Exercise 3: Check the index
# -----------------------------------------
# Instructions:
# Using this variable:
# Ask the user for their name.
# If their name is in the list,
# print the index of the FIRST occurrence of the name.
#
# Example:
# If input is 'Cortana'
# Output should be: 1
#
# Write your code below:

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name = input('What is your name?')
if name in names:
    print(names.index(name))

# =========================================
# Exercise 4: Greatest Number
# -----------------------------------------
# Instructions:
# Ask the user for 3 numbers.
# Print the greatest number.
num1 = int(input('please choose one number.'))
num2 = int(input('choose a second number.'))
num3 = int(input('choose a thrid number.'))
nums_lst = [num1,num2,num3]
print(max(nums_lst))

# Example:
# Input the 1st number: 25
# Input the 2nd number: 78
# Input the 3rd number: 87
#
# Output:
# The greatest number is: 87
#
# Write your code below:



# =========================================
# Exercise 5: The Alphabet
# -----------------------------------------
# Instructions:
# Create a string containing all letters of the alphabet.
# Loop over each letter.
# Print a message stating whether the letter
# is a vowel or a consonant.
#
# Write your code below:
alphabet = "abcdefghijklmnopqrstuvwxyz"

vowels = "aeiou"

for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")


# =========================================
# Exercise 6: Words and letters
# -----------------------------------------
# Instructions:
# Ask the user for 7 words.
# Store them in a list named words.
words = input('Give me 7 words.')
words_lst = words.split()
# Ask the user for a single character.
# Store it in a variable called letter.
letter = input('give me a character')
for i in words_lst:
    if letter in i : 
        print(i.index(letter))
    else:
        print(f'there is no such letter in the word {i}')
# Loop through the words list.
# For each word:
# - Print the index of the first appearance of the letter.
# - If the letter does not exist in the word,
#   print a friendly message with the word and the letter.
#
# Write your code below:



# =========================================
# Exercise 7: Min, Max, Sum
# -----------------------------------------
# Instructions:
# Create a list of numbers from 1 to 1,000,000.
lst = []
for i in range(1,1000001):
    lst.append(i)
[i for i in range(1,1000001)]
lst = list(range(1, 1000001))
# Use min() and max() to verify:
# - The list starts at 1
# - The list ends at 1,000,000
#
# Use sum() to calculate the total.
#
# Write your code below:



# =========================================
# Exercise 8: List and Tuple
# -----------------------------------------
# Instructions:
# Ask the user to enter comma-separated numbers.
nums = input("enter comma-separated number")
lst = nums.split(',')
tpl = tuple(lst)
# Generate:
# - A list containing every number.
# - A tuple containing every number.
#
# Example input:
# 34,67,55,33,12,98
#
# Expected output:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
#
# Write your code below:



# =========================================
# Exercise 9: Random number
# -----------------------------------------
# Instructions:
# Ask the user to input a number from 1 to 9 (inclusive).
num = input('input a number from 1 to 9 (inclusive)')
import random
number = random.randint(1, 9)
while True:
    num = input('input a number from 1 to 9 (inclusive)')
    if int(num) == number:
        print('Yes')
        break



# Generate a random number between 1 and 9.
# (Hint: use the random module)
#
# If the guess is correct:
#   Print "Winner"
#
# If the guess is incorrect:
#   Print "Better luck next time"
#
# Bonus:
# Use a loop that allows the user to keep guessing
# until they decide to quit.
#
# Write your code below:
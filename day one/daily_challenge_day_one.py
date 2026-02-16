# =========================================
# Daily Challenge: Build up a string
# Last Updated: October 30th, 2025
# =========================================

# 👩‍🏫 What You’ll Learn:
# - Python Basics
# - Conditionals
# - Loops


# =========================================
# Step 1: Ask for User Input
# =========================================

# Ask the user to enter a string.
# The string must be exactly 10 characters long.

word = input('Hi, please write a string that is 10 characters long.')

# =========================================
# Step 2: Check the Length of the String
# =========================================

# If the string is less than 10 characters,
# print: "String not long enough."

#if len(word) < 10 :
   # print("String not long enough.")


# If the string is more than 10 characters,
# print: "String too long."

#if len(word) > 10 :
  #  print('String too long.')

# If the string is exactly 10 characters,
# print: "Perfect string"
# and proceed to the next steps.

while len(word) != 10:
    if len(word) < 10 :
        print("String not long enough.")
    elif len(word) > 10 :
        print('String too long.')
    word = input('please write a string that is 10 characters long.')

if len(word) == 10: # not necessary
    print('Perfect string')



# =========================================
# Step 3: Print the First and Last Characters
# =========================================

# Once the string is validated,
# print the first character of the string.
# Then print the last character of the string.

print(f"{word[0]}\n{word[-1]}")

# =========================================
# Step 4: Build the String Character by Character
# =========================================

# Using a for loop,
# construct and print the string progressively:
# - First print the first character
# - Then the first two characters
# - Then the first three characters
# - Continue until the full string is printed
for i in range(10):
    print(word[:i+1])
# Hint:
# You can loop through the string
# and add one character at a time,
# printing the result at each step.


# =========================================
# Step 5 (Bonus): Jumble the String
# =========================================

# As a bonus,
# try shuffling the characters in the string
# and print the new jumbled version.
import random
lst = [char for char in word]
#new_lst = lst.random.shuffle()
random.shuffle(lst)
new_word = ''.join(lst)
for i in range(10):
    print(new_word[:i+1])

# Hint:
# You can use the random.shuffle function
# to shuffle a list of characters.
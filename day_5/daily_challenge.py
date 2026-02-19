# ==================================================
# 🏆 Daily Challenge
# Last Updated: October 7th, 2025
# ==================================================

# 👩‍🏫 What You’ll Learn
# - Python Basics
# - String Manipulation
# - Lists
# - Sorting
# - Functions


# ==================================================
# 🔹 Challenge 1: Sorting
# ==================================================
# Instructions:
# Write a Python program that takes a single string of words as input,
# where the words are separated by commas
# (example: "apple,banana,cherry").
#
# The program should output these words sorted in alphabetical order,
# separated by commas.


# -------------------------------
# Step 1: Get Input
# -------------------------------
# - Use input() to get a string from the user.
# - The words will be separated by commas.


user_input = input("Enter words separated by commas: ")
words_list = list(user_input.split(','))
sorted_words = sorted(words_list)


# -------------------------------
# Step 2: Split the String
# -------------------------------
# - Use the .split(',') method to convert the string
#   into a list of words.
#
# Example:
# words_list = user_input.split(',')


# -------------------------------
# Step 3: Sort the List
# -------------------------------
# - Use the sorted() function
#   OR the .sort() method to sort the list alphabetically.
#
# Example:
# sorted_words = sorted(words_list)


# -------------------------------
# Step 4: Join the Sorted List
# -------------------------------
# - Use the .join() method to convert the sorted list
#   back into a single string separated by commas.
#

result = ",".join(sorted_words)


# -------------------------------
# Step 5: Print the Result
# -------------------------------
# - Print the final string.
#

print(result)


# -------------------------------
# Expected Output:
# -------------------------------
# Input:  without,hello,bag,world
# Output: bag,hello,without,world


# ==================================================
# 🔹 Challenge 2: Longest Word
# ==================================================
# Instructions:
# Write a function that takes a sentence as input
# and returns the longest word in the sentence.
# If there are multiple longest words,
# return the first one encountered.
# Characters like apostrophes, commas, and periods
# should be considered part of the word.


# -------------------------------
# Step 1: Define the Function
# -------------------------------
# Define a function that takes a string
# (the sentence) as a parameter.
def max_word_in_sentence(str):
    sentence_list = list(str.split())
    length_list = [len(word) for word in sentence_list]
    max_length = max(length_list)
    for word in sentence_list:
          if len(word) == max_length:
            return word




# -------------------------------
# Step 2: Split the Sentence into Words
# -------------------------------


# -------------------------------
# Step 3: Initialize Variables
# -------------------------------


# -------------------------------
# Step 4: Iterate Through the Words
# -------------------------------


# -------------------------------
# Step 5: Compare Word Lengths
# -------------------------------


# -------------------------------
# Step 6: Return the Longest Word
# -------------------------------


# -------------------------------
# Expected Output:
# -------------------------------
print(max_word_in_sentence("Margaret's toy is a pretty doll.") )
# ➜ "Margaret's"
#
# longest_word("A thing of beauty is a joy forever.") 
# ➜ "forever."
#
# longest_word("Forgetfulness is by all means powerless!") 
# ➜ "Forgetfulness"

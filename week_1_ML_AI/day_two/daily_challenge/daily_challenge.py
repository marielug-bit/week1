
# ==================================================
# Challenge 1: Multiples of a Number
# ==================================================

# Key Python Topics:
# - input() function
# - Loops (for or while)
# - Lists and appending items
# - Basic arithmetic (multiplication)

# Instructions:
# 1. Ask the user for two inputs:
#    - A number (integer)
#    - A length (integer)

# 2. Create a program that generates a list of multiples
#    of the given number.
#
# 3. The list should stop when it reaches the length
#    specified by the user.
#
# Example 1:
# Input:
# number: 7
# length: 5
# Output:
# [7, 14, 21, 28, 35]
#
# Example 2:
# Input:
# number: 12
# length: 10
# Output:
# [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
#
# Example 3:
# Input:
# number: 17
# length: 6
# Output:
# [17, 34, 51, 68, 85, 102]

num = int(input('Choose an integer :'))
length = int(input('Choose a length : '))
lst = [num*i for i in range(1,length+1)]
print(lst)


# ==================================================
# Challenge 2: Remove Consecutive Duplicate Letters
# ==================================================

# Key Python Topics:
# - input() function
# - Strings and string manipulation
# - Loops (for or while)
# - Conditional statements (if)

# Instructions:
# 1. Ask the user for a string.

word = input("Choose a string: ")

new_word = word[0]  # on garde la première lettre

for i in range(1, len(word)):
    if word[i] != word[i-1]:
        new_word += word[i]

print(new_word)
    

#
# 2. Write a program that processes the string
#    to remove consecutive duplicate letters.
#
# 3. The new string should only contain unique
#    consecutive letters.
#
#    Example:
#    "ppoeemm" → "poem"
#    (remove consecutive duplicates like 'pp', 'ee', 'mm')
#
# 4. Print the modified string.
#
# Example 1:
# Input:
# "ppoeemm"
# Output:
# "poem"
#
# Example 2:
# Input:
# "wiiiinnnnd"
# Output:
# "wind"
#
# Example 3:
# Input:
# "ttiiitllleeee"
# Output:
# "title"
#
# Example 4:
# Input:
# "cccccaaarrrbbonnnnn"
# Output:
# "carbon"
#
# Notes:
# The final string will not include any consecutive duplicates.
# Non-consecutive duplicates are allowed.
# Example:
# In "recursive", the two 'r's and two 'e's are allowed
# because they are not consecutive.
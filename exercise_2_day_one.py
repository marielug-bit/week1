# =========================
# Exercise 1 : Hello World - I love Python
# Instructions:
# Print the following output in ONE line of code:
#
# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python
#
# Solution idea:
# Use string multiplication and concatenation in a single print statement.
# Example structure:
print(("Hello world\n" * 4) + ("I love python\n" * 4))


# =========================
# Exercise 2 : What is the Season ?
#
# Instructions:
# 1. Ask the user to input a month number (1 to 12).
# 2. Display the season corresponding to that month.
#
# Seasons:
# - Spring  : March (3) to May (5)
# - Summer  : June (6) to August (8)
# - Autumn  : September (9) to November (11)
# - Winter  : December (12) to February (2)
number = int(input('Please choose a number between 1 and 12.'))
if 3 <= number <= 5:
    print('This is Spring.')
if 6 <= number <= 8:
    print('This is Summer.')
if 9 <= number <= 11:
    print('This is Autumn.')
if number == 12 or 1 <= number <= 2:
    print('This is Winter.')
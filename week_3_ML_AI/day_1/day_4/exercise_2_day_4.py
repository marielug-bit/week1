# ==================================================
# What We Will Learn:
# - Functions
# ==================================================


# ==================================================
# 🌟 Exercise 1 : When Will I Retire?
# ==================================================
#
# Goal:
# Determine if a person can retire based on:
# - Their gender
# - Their date of birth
#
# Retirement Rules:
# - Men retire at age 67
# - Women retire at age 62 (born after April 1947)
#
# --------------------------------------------------
# Step 1: Create a function get_age(year, month, day)
#
# - Hard-code the current year and month in your code.
# - Calculate the person’s age.
# - Return the age as an integer.
current_year = 2026
current_month = 2
# --------------------------------------------------
# Step 2: Create a function can_retire(gender, date_of_birth)
#
# - This function should:
#     1. Call get_age() to calculate the person's age.
#     2. Determine retirement eligibility based on:
#           * Gender ("m" or "f")
#           * Age
#     3. Return:
#           True  → if the person can retire
#           False → if the person cannot retire
def get_age(year,month):
    if month > current_month:
        return current_year - year + 1
    if month <= current_month:
        return current_year - year


def can_retire(gender, date_of_birth):
    if gender == 'm':
        if get_age(date_of_birth) < 67:
            return False
        if get_age(date_of_birth) >= 67:
            return True
    if gender == 'f':
        if get_age(date_of_birth) < 62:
            return False
        if get_age(date_of_birth) >= 62:
            return True

# --------------------------------------------------
# Hints:
# - Ask the user for gender ("m" or "f")
# - Ask the user for date of birth in format: "yyyy/mm/dd"
# - Parse the date string into year, month, day
# - Call can_retire()
# - Display a message telling the user if they can retire
# - Test your code carefully


# ==================================================
# 🌟 Exercise 2 : Sum
# ==================================================
#
# Goal:
# Create a function that calculates:
#     X + XX + XXX + XXXX
#
# Example:
# If X = 3
# Result should be:
#     3 + 33 + 333 + 3333 = 3702
#
# Instructions:
# - Write a function that accepts one parameter (int: X)
# - Build the values:
#       X
#       XX
#       XXX
#       XXXX
# - Return the total sum
#
# Hint:
# - You may treat X as a string when repeating digits
# - Convert back to int when adding

def sum_4 (num):
    ls = []
    for index in range(1,5):
        str1 = str(num)*index
        ls.append(int(str1))
    return sum(ls)

# ==================================================
# 🌟 Exercise 3 : Double Dice
# ==================================================
#
# Goal:
# Simulate dice throws and analyze statistics.
#
# --------------------------------------------------
# Step 1: Create function throw_dice()
#
# - Simulate rolling one die
# - Return a random integer between 1 and 6
import random
def throw_dice():
    num = random.randint(1,6)
    return num
# --------------------------------------------------
# Step 2: Create function throw_until_doubles()
#
# - Roll two dice using throw_dice()
# - Keep rolling until both dice show the same number
# - Count how many throws it takes
# - Return the number of throws

def throw_until_doubles():
    count = 1
    num1 = throw_dice()
    num2 = throw_dice()
    print((num1,num2), end= ' ')
    while num1 != num2:
        num1 = throw_dice()
        num2 = throw_dice()
        print((num1,num2), end= ' ')
        count+=1
    return count
# Example:
# (1,2), (3,1), (5,5)
# → Stop at (5,5)
# → Return 3
#
# --------------------------------------------------
# Step 3: Create main()
#
# - Call throw_until_doubles() 100 times
# - Store the number of throws needed each time
#   (Choose an appropriate data structure)

def main():
    ls = []
    for i in range(1,101):
        num = throw_until_doubles()
        ls.append(num)
    print(sum(ls))
    print(sum(ls)/len(ls))
    print(round(sum(ls)/len(ls),2))

# After 100 simulations:
# - Print:
#       Total number of throws to reach 100 doubles
# - Print:
#       Average number of throws needed
# - Round average to 2 decimal places
#
# Example Output:
# Total throws: 8
# Average throws to reach doubles: 2.67
#
# --------------------------------------------------
# Notes:
# - Use random module
# - Use loops
# - Use collections (list recommended)
# - Use round() for formatting average
# ==================================================
# Good luck! 🚀
# ==================================================
# ==================================================
# 🧠 Daily Challenge : Advanced Algorithm
# Last Updated: February 5th, 2026
# ==================================================
#
# 👩‍🏫 What You will learn :
# - Python Basics
# - Conditionals
# - Loops
# - Functions
#
# ==================================================
# Instructions
# ==================================================
# Here is a python code that generates a list of 20000 random numbers,
# called list_of_numbers, and a target number.
#
import random
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728
for number in list_of_numbers[0:10001]:
    if target_number - number in list_of_numbers:
        print(f'{number} and {target_number - number} sum to the target_number {target_number}. ')
#
# Copy this code, and create a program that finds, within list_of_numbers,
# all the pairs of numbers that sum to the target_number.
#
# Examples of valid pairs:
# - 1000 and 2728 sum to the target_number 3728
# - 1864 and 1864 sum to the target_number 3728
#
# One Last Thing: Good luck!

seen = set()
pairs = set()

for number in list_of_numbers:
    complement = target_number - number
    
    if complement in seen:
        # on trie pour éviter les doublons inversés
        pair = tuple(sorted((number, complement)))
        pairs.add(pair)
    
    seen.add(number)

for a, b in pairs:
    print(f"{a} and {b} sum to {target_number}")
#==================================================
# 🌟 Exercise 1 : Cars
# ==================================================
#
# Instructions:
#
# 1️⃣ Copy this string into your code:
cars = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
#
# 2️⃣ Convert the string into a list using Python.
#    ⚠️ Do NOT convert it manually.
#    (Hint: use .split())
cars_list = cars.split(", ")
#
# 3️⃣ Print a message saying how many manufacturers
#    (companies) are in the list.
print(f'there are {len(cars_list)} manufacturers in the list  ')
# 4️⃣ Print the list of manufacturers in reverse
#    alphabetical order (Z-A).
#    (Hint: use sorted() with reverse=True)
new_list = sorted(cars_list,reverse=True)
for manufacturer in new_list :
    print(manufacturer, end = " ")
#
# --------------------------------------------------
# Using loops or list comprehension:
#
# 5️⃣ Count how many manufacturers’ names
#    contain the letter 'o'.
count = 0
for manufacturer in cars_list:
    count += manufacturer.lower().count('o')
#
# 6️⃣ Count how many manufacturers’ names
#    do NOT contain the letter 'i'.
count = 0
for manufacturer in cars_list:
    if not manufacturer.lower().count('o'):
        count+=1 

#
# --------------------------------------------------
# 🔥 Bonus 1:
#
# Given this list (with duplicates):
#
# ["Honda","Volkswagen", "Toyota",
#  "Ford Motor", "Honda",
#  "Chevrolet", "Toyota"]
#
# - Remove duplicates programmatically.
#   (Hint: you can use set())
#
# - Print the companies WITHOUT duplicates
#   in a comma-separated string
#   (no line breaks).
#   Example:
#   "Acura, Alfa Romeo, Aston Martin, ..."
#
# - Print a message saying how many
#   companies are now in the list.
#
# --------------------------------------------------
# 🔥 Bonus 2:
#
# - Print the list of manufacturers in
#   ascending alphabetical order (A-Z).
#
# - BUT reverse the letters of each
#   manufacturer’s name.
#
#   Example:
#   "Honda" → "adnoH"
#
# --------------------------------------------------
#
# One Last Thing:
# Good luck! 🚀
# ==================================================
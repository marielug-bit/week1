# ==================================================
# Exercises XP Ninja
# Last Updated: February 5th, 2026
# ==================================================
#
# What we will learn:
# - Functions
#
# ==================================================
# 🌟 Exercise 1 : What’s your name ?
# ==================================================
#
# Instructions:
# - Write a function called get_full_name() that takes 3 arguments:
#     1) first_name
#     2) middle_name (optional)
#     3) last_name
#
# - middle_name should be optional:
#     * If the user does NOT provide it, return only first + last
#     * If the user provides it, return first + middle + last
def get_full_name(first_name,last_name,middle_name=None):
    return first_name + last_name + middle_name


# Examples:
# - get_full_name(first_name="john", middle_name="hooker", last_name="lee")
#   → "John Hooker Lee"
#
# - get_full_name(first_name="bruce", last_name="lee")
#   → "Bruce Lee"
#
#
# ==================================================
# 🌟 Exercise 2 : From English to Morse
# ==================================================
#
# Instructions:
# - Write a function that converts English text to Morse code
# - Write another function that converts Morse code back to English
MORSE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--.."
}

def from_english_to_Morse(word):
    new_word = word.upper()
    for char in new_word:
        if char != ' ':
            letter = MORSE_DICT[char]
            print(letter, end= ' ')
        else:
            print('/ ')


def from_morse_to_english():
    pass

# Hint:
# - Use a translation table (dictionary) found online
# - Every letter is separated by a space
# - Every word is separated by a slash "/"
#
# Example format:
# "HELLO WORLD" -> ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
#
#
# ==================================================
# 🌟 Exercise 3 : Box of stars
# ==================================================
#
# Instructions:
# - Write a function named box_printer() that takes any amount of strings
#   (not inside a list) and prints them in a rectangular frame.
#
# - Print each word on its own line inside the box
# - The box width must fit the longest word
#
# Example:
# box_printer("Hello", "World", "in", "reallylongword", "a", "frame")
#
# Output:
# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************

def box_printer(*args):
    lst = list(args)
    length = len(lst[0])
    for word in lst:
        if len(word) > length:
            length = len(word)
    print('*'*(4+length))
    for word in lst:
        line = '* '+ word + (length-len(word))*' '+' *'
        print(line)
    print('*'*(4+length))

box_printer("Hello", "World", "in", "reallylongword", "a", "frame")
#
# ==================================================
# 🌟 Exercise 4 : What is the purpose of this code?
# ==================================================
#
# Instructions:
# - Analyze this code BEFORE executing it
# - What is the purpose of this code?
#
# Code:
def insertion_sort(alist):
   for index in range(1,len(alist)): #on parcour la liste

     currentvalue = alist[index] #a chaque boucle on definit une valeur de la liste
     position = index# a chaque boucle on retient l index

     while position>0 and alist[position-1]>currentvalue: # si on est pas dans la premiere boucle
         # et si le nombre d avant est superieur au nb actuel alors le nombre actuel devient le nombre d avan
         alist[position]=alist[position-1]
         position = position-1 

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)
#
#
# ==================================================
# One Last Thing: Good luck! 🚀
# ==================================================
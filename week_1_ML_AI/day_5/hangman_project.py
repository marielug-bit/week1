import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 
guessed_letters_list = []
num_mistake = 0
HANGMAN_PICS = [
"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
"""
]

def word_display(lst,word):
    star_word = list('*'*len(word))
    for index, value in enumerate(word):
        if value in lst:
            star_word[index] = value
    return''.join(star_word)

def is_choice_in_word(letter,word,num_mistake):
    if letter in word:
        if letter not in guessed_letters_list:
            guessed_letters_list.append(letter)
    else:
        num_mistake +=1
        update_gallow(num_mistake)
    return num_mistake

def end_of_the_game():
    if num_mistake == 6:
        print(f'Too many guesses, you just lost! the word was {word}.')
        return True
    if '*' not in word_display(guessed_letters_list,word):
        print('You won.')
        return True
    return False


def update_gallow(num):
    if num > 6:
        num = 6
    print(HANGMAN_PICS[num])


while True:
    print(word_display(guessed_letters_list,word))
    user_choice = input('Please write a letter: ').lower()
    num_mistake = is_choice_in_word(user_choice,word,num_mistake)
    if end_of_the_game():
        break



from anagram_checker import AnagramChecker


def display_menu(file_path):
    checker = AnagramChecker(file_path)
    while True:
        choice_str = input('ANAGRAMS CHECKER MENU \n Do you want to .... \n 1) check a word? \n 2)exit?')
        try :
            choice = int(choice_str)
            if choice == 1:
                word = (input('which word do you want to check? ')).lower()
                if checker.is_valid_word(word):
                    an_list = checker.get_anagrams(word)
                    print(f"Your word : {word} \n this is a valid English word. \n Anagrams for your word: {', '.join(an_list)}. ")
                else:
                    print('This is not a valid word.')
            if choice == 2:
                break
        except:
            print('Please answer by 1 or 2')
            continue


display_menu('/Users/mariekrammer/Desktop/week 1 ML AI/week_2_ML_AI/day_5/sowpods.txt')
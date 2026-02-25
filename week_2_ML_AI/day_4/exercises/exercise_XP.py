import random

def get_words_from_file(file_path):
    with open(file_path,'r') as f:
        content = f.read()
    list_of_words = content.splitlines()
    return list_of_words

#print(read_words())

def get_random_sentence(length,file_path):
    words = get_words_from_file(file_path)
    list_of_random_words = [random.choice(words) for i in range(length)]
    sentence = ' '.join(list_of_random_words)
    sentence = sentence.lower()
    return sentence

def main():
    print('You will choose a number, let s say 8. I will respond with a ' \
    'sentence of 8 words chosen randomly from a file')
    file_path = '/Users/mariekrammer/Desktop/week 1 ML AI/week_2_ML_AI/day_4/modules example/words.txt'
    length = input('what is the desired sentence length ? ')
    
    try :
        num = int(length)
        if num < 2 or num > 20:
            raise ValueError ("Number must be between 2 and 20")
        print(get_random_sentence(num,file_path))
    except ValueError:
        print('value error, this should be a number between 2 and 20')

main()
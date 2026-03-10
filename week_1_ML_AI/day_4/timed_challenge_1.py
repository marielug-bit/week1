word = input("Write something: " ).lower()
char = input('Write a character: ').lower()

def num_letter(word,char):
    print(word.count(char))


num_letter(word,char)
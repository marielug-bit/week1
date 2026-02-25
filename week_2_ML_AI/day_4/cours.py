import random

with open("day_4/modules example/words.txt",'r') as f:
    content = f.read()

words_list = content.splitlines()
print(words_list)

def get_words_from_file(file_path):
    with open(file_path,'r') as f:
        content = f.read()
    words_list = content.splitlines()
    return words_list

def get_random_sentence(length):
    try :

        word = ''
        for i in range(length):
            word_1 = random.choice(get_words_from_file("day_4/modules example/words.txt"))
            word += ' '+word_1
            # ici on ouvre 20 fois le fichier meme plus si length est plus grand, il vaut mieux creer une liste
            # et l appeler avant la boucle et faire randomchoice sur cette liste dans la boucle puis join
        return word.lower()
    
    except TypeError:
        print('this is not a number')

def main():
    length = (input('give me a length between 2 and 20 '))
    try :
        num = int(length)
        if num < 2 or num > 20:
            raise Exception
        get_words_from_file("day_4/modules example/words.txt")
        print(get_random_sentence(num))
    except:
        print('value error')

#main()



import json
sampleJson =  """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}""" 

data = json.loads(sampleJson)

print(data['company']['employee']['payable']['salary'])
data['company']['employee']["birth_date"] = "1990-05-15"

with open('employee.json','w') as f:
    json.dump(data,f,indent=2)

with open('employee.json','r') as f:
    content = f.read()

print(content)

import re

string = "at what time?"
match = re.search('at',string)
if (match):
    print ("String found at: " ,match.start())
else:
    print ("String not found!")
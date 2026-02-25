class Text:
    def __init__(self,text):
        self.text = text

    def word_frequency(self,word):
        list_of_words = self.text.split()
        amount = list_of_words.count(word)
        if not amount:
            print('no such word in the text')
        return amount
    
    def most_common_word(self):
        list_of_words = self.text.split()
        dic = {}
        for word in list_of_words:
            dic[word] = dic.get(word,0)+1
        max_word = max(dic, key = lambda k : dic[k])
        return max_word
    
    def unique_words(self):
        list_of_words = self.text.split()
        set_of_words = set(list_of_words)
        return list(set_of_words)


    @classmethod
    def from_file(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        text = Text(content)
        return text


import string
import re

class TextModification(Text):

    def remove_punctuation(self):
        modified_str = re.sub(rf"[{re.escape(string.punctuation)}]",'',self.text)
        return modified_str
    
    def remove_stop_words(self):
        list_of_words = self.text.split()
        new_list = list(filter(is_not_a_stop_word,list_of_words))
        return ' '.join(new_list)
    
    def remove_special_characters(self):
        cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return cleaned_text

    
    

def is_not_a_stop_word(word):
    stop_words = '''a, an, the, and, are, as, at, be, but, by, for, if, in, 
        into, is, it, no, not, of, on, or, such, that, 
        their, then, there, these, they, this, to, was, will, with'''
    stop_words_list = stop_words.replace("\n", "").split(', ')
    return word.lower() not in stop_words_list

class AnagramChecker:
    def __init__(self,text_file_path):
        with open (text_file_path, 'r') as f:
            self.text = list(map(str.lower,f.read().splitlines()))
    

    def is_valid_word(self,word):
        return word.lower() in self.text
    
    def is_anagram(self,word1,word2):
        word1_list = sorted(list(word1))
        word2_list = sorted(list(word2))
        return word1_list == word2_list
    
    def get_anagrams(self,word):
        anagrams_list = filter(lambda w: w != word and self.is_anagram(word,w),self.text)
        return anagrams_list

        






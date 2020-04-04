from functools import lru_cache
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:    
        concats = set() #set of concatenated words
        words_set = set(words) #set of all input words, for quick lookup
        
        @lru_cache(maxsize=15000)
        def is_concat(word):
            for i in range(len(word)):
                word_start = word[:i]
                word_end = word[i:]
                if word_start != "" and word_start in words_set: #check if beginning of word is in words_set
                    if word_end in words_set or is_concat(word_end): #check if end is in words_set, or is a concat
                        return True
            return False
        
        for word in words:
            if is_concat(word):
                concats.add(word)
        return list(concats)
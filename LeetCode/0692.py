class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict = {}
        for word in words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        
        #word_list = sorted(word_dict, key=lambda x: word_dict[x], reverse=True)
        #return word_list[:k]
        
        freq_dict = {}
        for key in word_dict:
            value = word_dict[key]
            if value not in freq_dict:
                freq_dict[value] = []
            freq_dict[value].append(key)
        
        freq_list = sorted(freq_dict, reverse=True) #create a sorted list of frequencies
        ordered_list = []
        for freq in freq_list:
            ordered_list += sorted(freq_dict[freq])
        
        return ordered_list[:k]
        
            
        
        
            
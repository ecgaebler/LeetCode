class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {} #maps a unique value for each letter
        s_pattern = [] #describes the pattern of letters relevant for testing isomorhpism
        s_num = 0 #counter for distinguishing between groups of different letters
        t_map, t_pattern, t_num = {}, [], 0 #same as above, but for t
        
        for letter in s:
            if letter not in s_map: #if letter hasn't been identified before
                s_map[letter] = s_num #add it to the map
                s_num += 1 #increase counter so next new letter gets a unique "ID"
            s_pattern.append(s_map[letter])
        
        for letter in t:
            if letter not in t_map:
                t_map[letter] = t_num
                t_num += 1
            t_pattern.append(t_map[letter])
        
        return s_pattern == t_pattern
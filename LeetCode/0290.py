class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        #words cannot fit pattern if their lengths don't match
        if len(words) != len(pattern) or len(words) == len(pattern) == 0:
            return False
        
        matched = {} #dictionary matching word to pattern char
        used_chars = set() #set of chars encountered so far
        for i in range(len(words)):
            #check if current word already matches a char other than the current char
            if words[i] in matched:
                if matched[words[i]] != pattern[i]:
                    return False
            #current word has not been seen before. Return false of current char has.
            elif pattern[i] in used_chars:
                return False
            else:
                matched[words[i]] = pattern[i]
                used_chars.add(pattern[i])
        
        return True
                
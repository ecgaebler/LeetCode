class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            key = ''.join(sorted(word)) #alphabetize key to ensure all anagrams will produce the same key
            if key in anagrams:         #check if this anagram already exists
                newlist = anagrams[key] #look up anagrams list for "key"
                newlist.append(word)    #add the newest word to anagram list
            else:
                anagrams[key] = [word] #key did not exist; add key:word pair to dictionary
        result = []
        for key in anagrams:
            result.append(anagrams[key])
        return result
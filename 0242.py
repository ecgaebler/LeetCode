class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #edge case with mismatched length
            return False
        s_letters = {} #dictionary of letters in s, and their frequency
        #record how many of what letter are in s
        for letter in s:
            if letter not in s_letters:
                s_letters[letter] = 0
            s_letters[letter] += 1
        #loop through t, checking against s_letters to determine if anagram
        for letter in t:
            if letter not in s_letters: #too many of this letter, or wrong type
                return False
            else:
                s_letters[letter] -= 1 #decrease number of remaining letters of this type
                if s_letters[letter] == 0:
                    del s_letters[letter] #ran out of this letter, so delete its entry
        if not s_letters: #if there are no entries, we've used every letter in s
            return True
        else:
            return False
                
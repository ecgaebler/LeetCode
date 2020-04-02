class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        prefixes = {"I":["V","X"], "X":["L","C"], "C":["D","M"]}
        result = 0
        prev_letter = ""
                    
        for letter in reversed(s): 
            if letter in prefixes and prev_letter in prefixes[letter]:
                result -= values[letter]
            else:
                result += values[letter]
            prev_letter = letter
        
        return result
            
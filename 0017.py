class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        valid_digits = set(["2","3","4","5","6","7","8","9"])
        for digit in digits: #catch invalid digit edge case
            if digit not in valid_digits:
                return []
        
        if len(digits) == 0: #catch empty edge case
            return []
        
        results = [] #solutions list
        letters = {} #dictionary mapping digits onto possible letters
        letters["2"] = ["a","b","c"]
        letters["3"] = ["d","e","f"]
        letters["4"] = ["g","h","i"]
        letters["5"] = ["j","k","l"]
        letters["6"] = ["m","n","o"]
        letters["7"] = ["p","q","r","s"]
        letters["8"] = ["t","u","v"]
        letters["9"] = ["w","x","y","z"]
        
        def permutations(digit_index, substring):
            """find all letter combinations after substring, given digit_index"""
            nonlocal results
            nonlocal digits
            nonlocal letters
            
            if digit_index >= len(digits): #reached end of number
                results.append(substring)  #add current string to results list
                return
            
            for letter in letters[digits[digit_index]]:
                permutations(digit_index + 1, substring + letter)
        
        permutations(0, "")
        return results
                
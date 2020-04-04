class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        magazine_chars = {}
        for char in magazine:
            if char not in magazine_chars:
                magazine_chars[char] = 1
            else:
                magazine_chars[char] += 1
        
        for char in ransomNote:
            if char not in magazine_chars:
                return False
            magazine_chars[char] -= 1
            if magazine_chars[char] == 0:
                del magazine_chars[char]
            
        return True
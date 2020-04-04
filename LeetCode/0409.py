class Solution:
    def longestPalindrome(self, s: str) -> int:
        max_length = 0
        unpaired = set()
        for char in s:
            if char in unpaired:
                unpaired.discard(char)
                max_length += 2
            else:
                unpaired.add(char)
        if len(unpaired) >= 1:
            max_length += 1
        return max_length
            
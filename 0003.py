class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0 #keep two pointers, one at the beginning of the window, one at the end
        longest = 0 #length of longest string
        active_chars = set()

        while right < len(s):
            
            if left == right:              #if window size is 0
                active_chars.add(s[right]) #add new element
                right += 1                 #expand window to include new element
            elif s[right] in active_chars:   #if next char is already in substring
                active_chars.remove(s[left]) #remove leftmost char
                left += 1                    #shrink window 
            else:                          #next char isn't in current string
                active_chars.add(s[right]) #add next char
                right += 1                 #expand window
                
            current_size = right - left
            if current_size > longest:
                longest = current_size
                
        return longest
                
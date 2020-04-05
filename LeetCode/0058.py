class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        found_nonspace = False #in case of trailing spaces at end
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if found_nonspace:
                    return length
            else:
                if not found_nonspace:
                    found_nonspace = True
                length += 1
        return length
        
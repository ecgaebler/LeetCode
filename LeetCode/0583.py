class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        #helper function to find largest common substring length
        def lcsl(w1, w2, len1, len2, calc_d):
            if len1 == 0 or len2 == 0:
                return 0
            #memoization
            if (w1, w2, len1, len2) in calc_d: 
                return calc_d[(w1, w2, len1, len2)]
            if w1[len1 - 1] == w2[len2 - 1]:
                result = 1 + lcsl(w1, w2, len1 - 1, len2 - 1, calc_d)
                calc_d[(w1, w2, len1, len2)] = result
                return result
            else:
                result = max(lcsl(w1, w2, len1 - 1, len2, calc_d), lcsl(w1, w2, len1, len2 - 1, calc_d))
                calc_d[(w1, w2, len1, len2)] = result
                return result
        
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        
        calculated = {}
        return len(word1) + len(word2) - 2 * lcsl(word1, word2, len(word1), len(word2), calculated)
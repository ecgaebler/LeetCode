class Solution:
    def countAndSay(self, n: int) -> str:
        def next_term(term):
            """ given a term, return the next term in the sequence """
            result = []
            prev_digit = term[0]
            count = 0
            for digit in term:
                if digit == prev_digit:
                    count += 1
                else:
                    result.append(str(count))
                    result.append(prev_digit)
                    prev_digit = digit
                    count = 1
            result.append(str(count))
            result.append(prev_digit)
            return result
                    
        term_num = 1
        result = ["1"]
        for _ in range(n-1):
            result = next_term(result)
        
        return ''.join(result)
            
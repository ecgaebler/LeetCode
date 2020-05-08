class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def helper (result, current_string, open_parens, close_parens):
            if close_parens == 0:
                result.append(current_string)
            if open_parens > 0:
                helper(result, current_string + "(", open_parens - 1, close_parens) 
            if close_parens > open_parens:
                helper(result, current_string + ")", open_parens, close_parens - 1)
        
        helper(result, "", n, n)
        return result
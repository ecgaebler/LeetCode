def isValid(s):
    open_brackets = "([{"
    close_brackets = ")]}"
    unclosed_parens = []
    def is_bracket_pair(a,b):
        if a == '(':
            return b == ')'
        if a == '[':
            return b == ']'
        if a == '{':
            return b == '}'
        return False
    
    for char in s:
        if char in close_brackets:
            if not unclosed_parens:
                return False
            if is_bracket_pair(unclosed_parens[-1], char):
                unclosed_parens.pop()
            else:
                return False
        elif char in open_brackets:
            unclosed_parens.append(char)
        else:
            return False
    if unclosed_parens:
        return False
    return True
    
    

def findTheDifference(s, t):
    s_letters = {}
    for char in s:
        if char not in s_letters:
            s_letters[char] = 0
        s_letters[char] += 1
    
    t_letters = {}
    for char in t:
        if char not in s_letters:
            return char
        if char not in t_letters:
            t_letters[char] = 0
        t_letters[char] += 1
        if t_letters[char] > s_letters[char]:
            return char
    
    return 0

def detectCapitalUse(word):
    all_lower = True
    all_upper = True
    init_cap = True
    if word[0].islower():
        init_cap = all_upper = False
    else:
        all_lower = False
        
    for i in range(1, len(word)):
        if word[i].isupper():
            init_cap = all_lower = False
        else:
            all_upper = False
        if not (all_lower or all_upper or init_cap):
            return False
        
    return all_lower or all_upper or init_cap

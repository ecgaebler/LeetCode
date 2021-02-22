def nextGreatestLetter(letters, target):
    l, r = 0, len(letters) - 1
    
    while l + 1 < r:
        mid = l + (r - l) // 2
        if ord(letters[mid]) < ord(target):
            l = mid
        else:
            r = mid
    
    if ord(letters[l]) > ord(target):
        return letters[0]
    elif ord(letters[l]) == ord(target):
        return letters[(l + 1) % len(letters)]
    elif ord(letters[r]) > ord(target):
        return letters[r]
    else:
        return letters[0]

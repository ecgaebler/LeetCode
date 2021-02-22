def nextGreatestLetter(letters, target):
    l, r = 0, len(letters) - 1
    
    while l + 1 < r:
        mid = l + (r - l) // 2
        if ord(letters[mid]) <= ord(target):
            l = mid
        else:
            r = mid
    
    if ord(letters[r]) <= ord(target):
        return letters[0]
    if ord(letters[l]) > ord(target):
        return letters[0]
    if ord(letters[l]) <= ord(target):
        return letters[r]
    return letters[l]

#TEST CODE
tests = [
    (["c","f","j"],"a","c"),
    (["c","f","j"],"c","f"),
    (["c","f","j"],"d","f"),
    (["c","f","j"],"g","j"),
    (["c","f","j"],"j","c"),
    (["c","f","j"],"k","c"),
    (["e","e","e","e","e","e","n","n","n","n"],"e","n"),
    (["e","e","e","e","e","e","n","n","n","n"],"n","e")]

do_tests = True
if do_tests:
    for letters, target, answer in tests:
        if nextGreatestLetter(letters, target) == answer:
            print("Test PASS") 
        else:
            print("Test FAIL")

def toLowerCase(s):
    charlist = []
    for char in s:
        if char.isupper():
            charlist.append(char.lower())
        else:
            charlist.append(char)
    return ''.join(charlist)

#TESTING
'''
tests = [
    "",
    "acdc",
    "c4s",
    "C6G",
    "4G"
    ]
for test in tests:
    print(toLowerCase(test))
'''

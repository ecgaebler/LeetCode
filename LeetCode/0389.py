def findTheDifference(s, t):
    s_sum = 0
    for char in s:
        s_sum += ord(char)
    
    t_sum = 0
    for char in t:
        t_sum += ord(char)
    
    return chr(t_sum - s_sum)

#TEST CODE
tests = [("abcd","abcde"),
         ("","y"),
         ("a","aa"),
         ("ae","eaa")]
for test in tests:
    print('input strings: "' + test[0] + '" & "' + test[1] + '"')
    print(" added char: '" + findTheDifference(test[0], test[1]) + "'")

"""
Write a function that takes in a string made up of brackets (such as "(", "[",
and "{") and other optional characters. The function should return wether the
string is balanced with regards to brackets.
example: "([])(){}(())()()" should return True because it's balanced.
"""

def balancedBrackets(string):
    brackets = [] #stack of unresolved brackets
    matches = {'(':')', '[':']', '{':'}', '<':'>'}
    
    for char in string:
        if char in matches.keys(): #char is an open bracket
            brackets.append(char)
        elif char in matches.values(): #char is a close bracket
            if not brackets:
                return False
            if matches[brackets.pop()] != char:
                return False

    return not brackets


#TEST CODE BELOW

#these should return False:
test0 = "("
test1 = "]"
test2 = "[{]}"
test3 = "[([)]]"
test4 = "{]"
test5 = "[)"

#these should return True:
test6 = ""
test7 = "a"
test8 = "()"
test9 = "([])"
testA = "([]{})"
testB = "[[]]"
testC = "a[bc(d)e{f}]gh"
testD = "()[]{}"
testE = "([{}])"
testF = "([])(){}(())()()"

tests = [test0, test1, test2, test3, test4, test5, test6, test7,
         test8, test9, testA, testB, testC, testD, testE, testF]

for test in tests:
    print(balancedBrackets(test))


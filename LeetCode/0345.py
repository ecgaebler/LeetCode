def reverseVowels(s):
    stack = []
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            stack.append(char)
            
    result = []
    for char in s:
        if char in vowels:
            result.append(stack.pop())
        else:
            result.append(char)
    
    return ''.join(result)
                

#TEST CODE
test_inputs = ["hello","leetcode","","o","x","oxa","xox","xaex"]
test_expects = ["holle","leotcede","","o","x","axo","xox","xeax"]
for i, test in enumerate(test_inputs):
    print(reverseVowels(test) == test_expects[i])

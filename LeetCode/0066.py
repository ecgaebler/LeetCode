'''
Given a non-empty array of decimal digits representing a non-negative integer,
increment one to the integer.

The digits are stored such that the most significant digit is at the head of
the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number
0 itself.


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
'''
def plusOne(digits):
    increment = True
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    digits.insert(0, 1)
    return digits

#TEST CODE
tests = ([1,2,3],
         [5,9],
         [9],
         [0])

answers = ([1,2,4],
           [6,0],
           [1,0],
           [1])
print("test inputs: ", tests)
for i, test in enumerate(tests):
    if plusOne(test) == answers[i]:
        print("test PASSED")
    else:
        print("test FAIL")
print("test outputs: ", tests)

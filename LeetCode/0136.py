'''
Given a non-empty array of integers nums, every element
appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear
runtime complexity and without using extra memory?
'''

def singleNumber(nums):
    for i in range(1, len(nums)):
        nums[0] ^= nums[i]
    return nums[0]

'''
Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one
element which appears only once.
'''

#TEST CODE
tests = ([2,2,1],
         [4,1,2,1,2],
         [-5],
         [0,1,7,1,0])
answers = (1, 4, -5, 7)
for i, test in enumerate(tests):
    test_str = str(test)
    if singleNumber(test) == answers[i]:
        print("test PASS")
    else:
        print("test FAIL")
        print("  input: " + test_str)
        print("  expected output: " + str(answers[i]))
        print("  actual output: " + str(test[0]))

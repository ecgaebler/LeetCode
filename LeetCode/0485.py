def findMaxConsecutiveOnes(nums):
    max_ones = 0
    current_ones = 0
    for value in nums:
        if value == 0:
            max_ones = max(max_ones, current_ones)
            current_ones = 0
        else:
            current_ones += 1
    return max(max_ones, current_ones)

#TESTING CODE
tests = [([1,0,1,1,0,1], 2),
         ([1], 1),
         ([0], 0),
         ([1,0], 1),
         ([0,1], 1),
         ([1,1,0,1], 2),
         ([1,0,1,1], 2),
         ([0,0,0], 0)]
for test in tests:
    print(findMaxConsecutiveOnes(test[0]) == test[1])

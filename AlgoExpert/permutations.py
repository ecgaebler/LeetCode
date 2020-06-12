"""
Write a function that takes in an array of unique integers and returns an
array of all permutations of those integers, in no particular order.
If the input is empty, the function should return an empty array.
"""

def getPermutations(array):
    if len(array) == 1:
        return [array]
    if len(array) == 0:
        return []
    result = []
    for i, num in enumerate(array):
        #add current num to beginning of all permutations that exclude it
        for perm in getPermutations(array[:i] + array[i+1:]):
            result.append([num] + perm)
    return result

#TEST CODE:
'''
test0 = [1,2,3]
test1 = []
test2 = [5]
tests = [test0, test1, test2]
for test in tests:
    print(f"{test} —> {getPermutations(test)}")
    
'''

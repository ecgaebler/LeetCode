"""
Write a function that takes in an array of unique integers and returns its
powerset. The powerset of a set S is the set of all subsets of S.
"""

def powerset(array):
    result = [[]]
    for i in range(len(array)):
        current_len = len(result)
        for j in range(current_len):
            #current_len is used because the length of result changes as we
            #append new elements to it, and we don't want an infinite loop
            result.append(result[j] + [array[i]])
    return result

#TESTING CODE:
"""
for i in range(4):
    print(f"{[_+1 for _ in range(i)]} —> {powerset([_+1 for _ in range(i)])}")
"""

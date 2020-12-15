def findShortestSubArray(nums):
    if len(nums) == 0:
        return 0
    most_frequent = []
    max_freq = 0
    frequencies = {}
    endpoints = {}
    for i, num in enumerate(nums):
        if num not in frequencies:
            frequencies[num] = 1
            endpoints[num] = [i, i]
        else:
            frequencies[num] += 1
            endpoints[num][1] = i
            
        if frequencies[num] > max_freq:
            max_freq = frequencies[num]
            most_frequent = [num]
        elif frequencies[num] == max_freq:
            most_frequent.append(num)
    
    min_size = len(nums)
    for num in most_frequent:
        span = endpoints[num][1] - endpoints[num][0] + 1
        if span < min_size:
            min_size = span
    return min_size


#TESTING
'''
tests = [
    [1,2,2,3,1],    #should be 2
    [1,2,2,3,1,4,2],#should be 6
    [9],            #should be 1
    [],             #should be 0
    [1,2],          #should be 1
    [1,2,1,0]       #should be 3
    ]
for test in tests:
    print(findShortestSubArray(test))   
'''

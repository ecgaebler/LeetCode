def arrayPairSum(nums):
    nums.sort()
    min_sum = 0
    for i in range(len(nums)//2):
        min_sum += nums[2*i]
    return min_sum
#The idea behind this algorithm is that if we "use up" as many of the
#smallest values as we can by putting them in pairs with other smallest
#numbers. For example, when counting the min values in the pairs, any pair
#that includes the smallest value will contribute that smallest value. The
#second smallest value will also dominate its pair, unless it is paired 
#with the single smallest value. If you pair it that way, the third 
#smallest value will get counted while the second smallest won't.

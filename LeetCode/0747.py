class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest_index = 0
        if len(nums) == 1:
            return largest_index
        largest = float("-inf")
        second_largest = float("-inf")
        for i, num in enumerate(nums):
            if num > largest:
                second_largest = largest
                largest = num
                largest_index = i
            else:
                second_largest = max(second_largest, num)
        if largest >= 2*second_largest:
            return largest_index
        return -1
        
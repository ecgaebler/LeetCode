class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurances = {}
        n = len(nums)
        for num in nums:
            if num not in occurances:
                occurances[num] = 0
            occurances[num] += 1
            if occurances[num] > n//2:
                return num
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        uncounted = set(_ for _ in range(1, len(nums) + 1))
        for num in nums:
            uncounted.discard(num)
        return list(uncounted)
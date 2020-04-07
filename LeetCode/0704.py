class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid
            if nums[mid] >= target:
                r = mid
        if nums[r] == target:
            return r
        if nums[l] == target:
            return l
        return -1
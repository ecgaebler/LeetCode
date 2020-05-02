class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, candidate = 0, 0
        for i in range(len(nums)):
            if count <= 0: #replace candidate
                candidate = nums[i]
                count = 1
            else:
                if nums[i] == candidate:
                    count += 1
                else:
                    count -= 1
        return candidate
            
                
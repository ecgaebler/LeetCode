class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        other_nums = set()
        if len(nums1) <= len(nums2):
            nums = nums1
            other_nums = set(nums2)
        else:
            nums = nums2
            other_nums = set(nums1)
            
        result = set()
        for num in nums:
            if num in other_nums:
                result.add(num)
                
        return list(result)
                    
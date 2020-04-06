class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        def first_between(array, target, l, r):
            """ Find the first instance of a value between index l and r. """
            l, r = 0, len(array) - 1
            while l + 1 < r:
                mid = l + (r - l) // 2
                if array[mid] < target:
                    l = mid
                else:
                    r = mid
            #post-processing
            if array[l] == target:
                return l
            elif array[r] == target:
                return r
            return -1
        
        def last_between(array, target, l, r):
            """ Find the last instance of a value between index l and r. """
            l, r = 0, len(array) - 1
            while l + 1 < r:
                mid = l + (r - l) // 2
                if array[mid] <= target:
                    l = mid
                else:
                    r = mid
            #post-processing
            if array[r] == target:
                return r
            elif array[l] == target:
                return l
            return -1
        
        #binary search until you find the target, then split from there
        start, end = 0, len(nums) - 1
        while start + 1 < end:
                mid = start + (end - start) // 2
                if nums[mid] < target:
                    start = mid
                elif nums[mid] > target:
                    end = mid
                else: #if nums[mid] == target, split binary search from here to find both edges.
                    break
        first_target = first_between(nums, target, start, end)
        last_target = last_between(nums, target, start, end)
        return [first_target, last_target]
                
        return [-1,-1]
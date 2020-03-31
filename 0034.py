class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findFirst(nums, target):
            start = 0
            end = len(nums) - 1
        
            while start <= end:
                mid = start + (end - start) // 2
            
                if nums[mid] == target:
                    if (mid == 0 or target > nums[mid-1]):
                        return mid
                    else:
                        end = mid - 1
                elif target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
                    
            return -1
        
        def findLast(nums, target):
            start = 0
            end = len(nums) - 1
            
            while start <= end:
                mid = start + (end - start) // 2
                
                if nums[mid] == target:
                    if (mid == len(nums)-1 or target < nums[mid+1]):
                        return mid
                    else:
                        start = mid + 1
                elif target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            
            return -1
        
        return [findFirst(nums, target), findLast(nums, target)]
    
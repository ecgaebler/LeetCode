class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return
        low, unsorted, high = 0, 0, len(nums) - 1
        
        while (high >= unsorted):
            
            if nums[unsorted] == 0: #ball is red
                temp = nums[low]
                nums[low] = nums[unsorted]
                nums[unsorted] = temp
                low += 1 #balls swapped
                unsorted += 1 #look at next
                
            elif nums[unsorted] == 1: #ball is white
                unsorted += 1 #already sorted, look at next.
                
            else: #ball must be blue
                temp = nums[unsorted]
                nums[unsorted] = nums[high]
                nums[high] = temp
                high -= 1 #one more blue ball at end
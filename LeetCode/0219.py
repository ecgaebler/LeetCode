class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        active = set() #numbers within sliding window
        left = 0 #index of left side of sliding window
        
        for right in range(len(nums)):
            #advance start of window to maintain max window size
            if right - left > k:
                active.discard(nums[left]) 
                left += 1
            #check for matches within active window
            if nums[right] in active:
                return True
            active.add(nums[right])
        return False
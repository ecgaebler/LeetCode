class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicated_nums = set()
        duplicates = {}
        
        #record duplicates and their indices
        for i, num in enumerate(nums):
            if num not in duplicates:
                duplicates[num] = []
            else:
                duplicated_nums.add(num)
            duplicates[num].append(i)
        
        for num in duplicates:
            #check pairs of indices for duplicated values. indices list should already be sorted.
            for i in range(len(duplicates[num]) - 1):
                if duplicates[num][i+1] - duplicates[num][i] <= k:
                    return True
        
        return False
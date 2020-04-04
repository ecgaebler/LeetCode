class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        sorted_nums = sorted(nums) #sort now, so all solutions will automatically have elements sorted
        solutions = set() #Set of all solutions found so far
        result = [] #List of solutions, to be returned at end of function
        
        target_nums = {} #dictionary of all values and their possible indices
        for index, num in enumerate(sorted_nums):
            if num not in target_nums:
                target_nums[num] = [] #initialize list of indices with value "num"
            target_nums[num].append(index) #add this index to list of indices with value "num"
            
        nums_len = len(sorted_nums) 
        for i in range(nums_len-2):
            for j in range(i+1, nums_len-1):
                target = -1 * (sorted_nums[i] + sorted_nums[j]) #we want to check if this value exists in target_nums
                if target in target_nums: 
                    largest_index = target_nums[target][-1] 
                    if largest_index > j: #check if index is greater than j, to make sure we don't double-count
                        solution = (sorted_nums[i], sorted_nums[j], target)
                        if solution not in solutions:
                            solutions.add(solution)
                            result.append([solution[0], solution[1], solution[2]])
            
        return result
            
        
        
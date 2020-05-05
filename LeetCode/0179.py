class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        #compare both concatenation orders to determine num with higher rank
        def higher_rank(num1, num2):
            """ Returns True if num1 has higher rank than num2 """
            return int(num1 + num2) > int(num2 + num1)
                
        def binary_search_insert(num, array):
            """ Returns the index where num should be inserted in array """
            if len(array) == 0:
                return 0
            l, r = 0, len(array)
            while l + 1 < r:
                mid = l + (r - l) // 2
                if higher_rank(num, array[mid]):
                    r = mid
                else:
                    l = mid
            
            if higher_rank(num, array[l]):
                return l
            else:
                return r
        
        #Convert nums into strings, then use binary search to build sorted list
        sorted_nums = []
        for num in nums:
            str_num = str(num)
            sorted_nums.insert(binary_search_insert(str_num, sorted_nums), str_num)
            
        #Check for edge case with only 0 in nums
        if len(sorted_nums) > 0 and sorted_nums[0] == "0":
            return "0"
            
        #combine the sorted list to get final, largest number
        return ''.join(sorted_nums)
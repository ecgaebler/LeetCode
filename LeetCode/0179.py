class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def higher_rank(num1, num2):
            """ returns True if num1 is higher ranked than num2"""
            for i in range(max(len(num1), len(num2))):
                if i >= len(num2): #num1 is longer
                    if num1[i] > num1[0]: #compare next digit against first digit
                        return True
                    return False
                if i >= len(num1): #num2 is longer
                    if num2[i] > num1[0]:
                        return False
                    return True
                if num1[i] > num2[i]:
                    return True
                if num1[i] < num2[i]:
                    return False
            return False #num1 and num2 must be the same
                
        def binary_search_insert(num, array):
            """ returns the index where num should be inserted"""
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
        
        sorted_nums = []
        for num in nums:
            str_num = str(num)
            sorted_nums.insert(binary_search_insert(str_num, sorted_nums), str_num)
            
        if len(sorted_nums) > 0 and sorted_nums[0] == "0":
            return "0"
            
        return ''.join(sorted_nums)
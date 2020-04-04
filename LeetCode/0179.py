class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def higher_rank(num1, num2):
            """ returns True if num1 is higher ranked than num2"""
            i, j = 0, 0
            while i < len(num1) or j < len(num2):
                #reached end of num1
                if i == len(num1):
                    if num1[0] > num2[j]:
                        return True
                    if num1[0] < num2[j]:
                        return False
                    j += 1
                    continue
                #reached end of num2
                if j == len(num2): 
                    if num1[i] > num2[0]:
                        return True
                    if num1[i] < num2[0]:
                        return False
                    i += 1
                    continue
                if num1[i] > num2[i]:
                    return True
                if num1[i] < num2[i]:
                    return False
                i += 1
                j += 1
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

'''
#Test cases:
#note that it fails for [121,12].
[10,2]
[]
[0]
[0,0]
[121,12]
[24, 75, 814, 691, 94, 324, 627, 816, 138, 974, 2, 214, 661, 269, 942, 850, 640, 563, 405, 69, 293, 876, 377, 76, 62, 782, 23, 259, 231, 233]
[4704,6306,9385,7536,3462,4798,5422,5529,8070,6241,9094,7846,663,6221,216,6758,8353,3650,3836,8183,3516,5909,6744,1548,5712,2281,3664,7100,6698,7321,4980,8937,3163,5784,3298,9890,1090,7605,1380,1147,1495,3699,9448,5208,9456,3846,3567,6856,2000,3575,7205,2697,5972,7471,1763,1143,1417,6038,2313,6554,9026,8107,9827,7982,9685,3905,8939,1048,282,7423,6327,2970,4453,5460,3399,9533,914,3932,192,3084,6806,273,4283,2060,5682,2,2362,4812,7032,810,2465,6511,213,2362,3021,2745,3636,6265,1518,8398]
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        #include dp dictionary
        def unique_subtrees(min_num, max_num):
            if max_num == min_num + 1:
                return 1
            result = 0
            for num in range(min_num, max_num):
                left_subtrees = unique_subtrees(min_num, num)
                right_subtrees = unique_subtrees(num + 1, max_num)
                result = result + left_subtrees + right_subtrees
            return result
        
        return unique_subtrees(1, n + 1)
        
        #also consider mathematical approach
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        #find row index
        l, r = 0, len(matrix) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if matrix[mid][0] > target:
                r = mid
            else:
                l = mid
        if matrix[r][0] <= target:
            row = r
        else:
            row = l
            
        #find element index
        l, r = 0, len(matrix[0]) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if matrix[row][mid] > target:
                r = mid
            else:
                l = mid
        return matrix[row][r] == target or matrix[row][l] == target
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        temp = []
        n = len(matrix)
        for ring in range(n // 2):
            for step in range(ring, n-1 - ring):
                #cell0 = matrix[ring][step]
                #cell1 = matrix[step][n-1 - ring]
                #cell2 = matrix[n-1 - ring][n-1 - step]
                #cell3 = matrix[n-1 - step][ring]
                temp = matrix[n-1 - step][ring]
                matrix[n-1 - step][ring] = matrix[n-1 - ring][n-1 - step]
                matrix[n-1 - ring][n-1 - step] = matrix[step][n-1 - ring]
                matrix[step][n-1 - ring] = matrix[ring][step]
                matrix[ring][step] = temp
        return
        
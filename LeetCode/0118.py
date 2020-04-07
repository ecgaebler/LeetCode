class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = [[1]]
        if numRows >= 2:
            result.append([1,1])
        if numRows >= 3:
            while len(result) < numRows:
                prev_row_len = len(result[-1])
                result.append([1])
                for i in range(prev_row_len - 1):
                    result[-1].append(result[-2][i] + result[-2][i + 1])
                result[-1].append(1)
                
        return result
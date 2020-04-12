class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        result = []
        for i in range(len(T)):
            if i >= len(T) - 1:
                result.append(0)
                break
            count = 0
            for j in range(i+1, len(T)):
                if T[j] > T[i]:
                    count = j - i
                    break
            result.append(count)
        return result
                        
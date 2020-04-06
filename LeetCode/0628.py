class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        most_positive = [float("-inf"), float("-inf"), float("-inf")]
        most_negative = [0,0]
        
        for num in nums:
            if num > most_positive[0]:
                if num <= most_positive[1]:
                    most_positive[0] = num
                elif num <= most_positive[2]:
                    most_positive[0] = most_positive[1]
                    most_positive[1] = num
                else:
                    most_positive[0] = most_positive[1]
                    most_positive[1] = most_positive[2]
                    most_positive[2] = num
                    
            if num < most_negative[1]:
                if num < most_negative[0]:
                    most_negative[1] = most_negative[0]
                    most_negative[0] = num
                else:
                    most_negative[1] = num
        
        return most_positive[2] * max(most_positive[0] * most_positive[1], most_negative[0] * most_negative[1])
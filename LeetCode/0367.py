class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 0:
            return False
        
        def sqrt_estimate(square):
            estimate = square >> square.bit_length()//2
            while abs(estimate**2 - square) > 1:
                estimate = (estimate + square/estimate)/2.0
            return int(estimate)
        
        estimate = sqrt_estimate(num)
        return estimate**2 == num
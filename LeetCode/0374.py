# NOTE: This won't actually run as is. This is just what I submitted on LeetCode.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l + 1 < r:
            mid = l + (r - l) // 2
            if guess(mid) < 0:
                r = mid
            elif guess(mid) > 0:
                l = mid
            else:
                return mid
        if guess(l) == 0:
            return l
        if guess(r) == 0:
            return r
        return -1

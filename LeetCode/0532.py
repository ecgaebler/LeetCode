class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        if k == 0:
            doubles = set()
            counted = set()
            for num in nums:
                if num in counted:
                    doubles.add(num)
                counted.add(num)
            return len(doubles)
        
        counted = set()
        pairs = set()
        for num in nums:
            if num not in counted:
                counted.add(num)
                if num - k in counted:
                    pairs.add((num - k, num))
                if num + k in counted:
                    pairs.add((num, num + k))
                    
        return len(pairs)
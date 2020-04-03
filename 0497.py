from random import randint
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        current_end = 0
        for rect in rects:
            x1, y1, x2, y2 = rect
            width = 1 + abs(x2-x1)
            height = 1 + abs(y2-y1)
            current_end += width * height
            self.weights.append(current_end)

    def pick(self) -> List[int]:
        def binary_search(target):
            """returns the index of rect corresponding to chosen number"""
            l, r = 0, len(self.weights) - 1
            while l + 1 < r:
                mid = l + (r - l) // 2
                if self.weights[mid] < target:
                    l = mid
                else:
                    r = mid
            if self.weights[r] >= target:
                return r
            return l
        rand_number = randint(1,self.weights[-1])
        x1, y1, x2, y2 = self.rects[binary_search(rand_number)]
        return [randint(x1, x2), randint(y1, y2)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
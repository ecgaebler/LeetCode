from random import randint
from bisect import bisect_left
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        current_end = 0
        for rect in rects:
            x1, y1, x2, y2 = rect
            width = 1 + x2 - x1
            height = 1 + y2 - y1
            current_end += width * height
            self.weights.append(current_end)

    def pick(self) -> List[int]:
        rand_number = randint(1,self.weights[-1])
        x1, y1, x2, y2 = self.rects[bisect_left(self.weights, rand_number)]
        return [randint(x1, x2), randint(y1, y2)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
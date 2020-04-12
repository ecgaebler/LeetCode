# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root or root.val == None:
            return []
        result = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, row = queue.popleft()
            if row + 1 > len(result):
                result.append(node.val)
            else:
                result[row] = max(result[row], node.val)
            if node.right:
                queue.append((node.right, row + 1))
            if node.left:
                queue.append((node.left, row + 1))
        return result
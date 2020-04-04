# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        if not root:
            return max_depth
        queue = deque()
        queue.append((root,1))
        while(queue):
            node, depth = queue.popleft()
            if depth > max_depth:
                max_depth = depth
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return max_depth
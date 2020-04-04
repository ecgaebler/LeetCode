# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: #check for null root
            return True
        left_queue = deque()
        left_queue.append(root.left)
        right_queue = deque()
        right_queue.append(root.right)
        while right_queue or left_queue:
            left_node = left_queue.popleft()
            right_node = right_queue.popleft()
            if not left_node or not right_node: #check for null nodes
                if left_node != right_node: 
                    return False
                else:
                    continue #both nodes must be null
            if left_node.val != right_node.val:
                return False
            left_queue.append(left_node.left)
            left_queue.append(left_node.right)
            right_queue.append(right_node.right)
            right_queue.append(right_node.left)
        return True
            
        
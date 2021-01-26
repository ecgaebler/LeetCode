# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def height(node):
            if not node: 
                return (0)
            left_height = height(node.left)
            right_height = height(node.right)
            if left_height < 0 or right_height < 0:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)
        
        height = height(root)
        return height > 0

'''
TEST CASES USED ON LEETCODE
[3,9,20,null,null,15,7]
[1,2,2,3,3,null,null,4,4]
[1,null,null]
[]
[1,null,2,null,3]
[1,2,3,4,5,6,null,8]
'''

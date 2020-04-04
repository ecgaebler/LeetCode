# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def evalBST(node, min_val = float("-inf"), max_val = float("inf")):
            if not node: #empty branch is always balanced
                return True
            if node.val == None:
                return True #invalid BST
            if not min_val < node.val < max_val:
                return False #node's value must be strictly less than min_val and greater than max_val
            
            return evalBST(node.left, min_val, node.val) and evalBST(node.right, node.val, max_val)
        return evalBST(root)
        
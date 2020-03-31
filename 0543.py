# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_diameter = 0
        
        def max_length(Node):
            nonlocal max_diameter
            if not Node: 
                return 0 #null node cannot contribute
            left = max_length(Node.left) #length of left branch
            right = max_length(Node.right) #length of right branch
            reset_diameter = left + right #diameter if we use Node as new root
            max_diameter = max(max_diameter, reset_diameter)
            return 1 + max(left, right) #max length between using left and right branches
        
        max_length(root)
        return max_diameter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        #returns the greatest sum of values possible for a path through a binary tree
        self.max_sum = float("-inf")
        
        def max_contribution(node):
            """returns the largest contribution a node can contribute to a path"""
            if not node:
                return 0
            left_sum = max(0,max_contribution(node.left)) #left sum, or 0 if sum is negative
            right_sum = max(0,max_contribution(node.right)) #same with right subtree
            new_path_cost = node.val + max(0, left_sum) + max(0, right_sum)
            self.max_sum = max(new_path_cost, self.max_sum) #update if restarting at this node gives better sum
            return node.val + max(left_sum, right_sum)
        
        max_contribution(root)
        return self.max_sum
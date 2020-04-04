# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        def largest_node(node):
            largest = node
            while(largest.right != None):
                largest = largest.right
            return largest
    
        def deleteNodeHelper(root, key):
        
            if root == None: #base case
                return root
        
            if key < root.val: #check left branch
                root.left = deleteNodeHelper(root.left, key)
        
            elif key > root.val: #check right branch
                root.right = deleteNodeHelper(root.right, key)
        
            else:
                if root.left == None: #no left branch
                    return root.right
                elif root.right == None: #no right branch
                    return root.left
                else: #both branches present
                    new_root = largest_node(root.left)
                    root.val = new_root.val
                    root.left = deleteNodeHelper(root.left, new_root.val)
            
            return root
        
        return deleteNodeHelper(root, key)

            
            
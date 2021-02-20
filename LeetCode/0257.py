#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    if not root:
        return []
    
    def findPaths(node):
        if not node.right and not node.left: #leaf node
            return [str(node.val)]
        result = []
        if node.right:
            for path in findPaths(node.right):
                result.append(str(node.val) + "->" + path)
        if node.left:
            for path in findPaths(node.left):
                result.append(str(node.val) + "->" + path)
        return result
    
    return findPaths(root)

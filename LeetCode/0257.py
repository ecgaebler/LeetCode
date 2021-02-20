#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    if not root:
        return []
    if not root.right and not root.left:
        return [str(root.val)]
    
    def findPaths(node, pathSoFar, result):
        currentPath = pathSoFar + "->" + str(node.val)
        if not node.right and not node.left: #leaf node
            result.append(currentPath)
            return
        if node.right:
            findPaths(node.right, currentPath, result)
        if node.left:
            findPaths(node.left, currentPath, result)
    
    result = []
    findPaths(root, "", result) 
    return result

def invertBinaryTree(tree):
    def recurse_inverse(root):
		if root is None:
			return
		root.left, root.right = recurse_inverse(root.right), recurse_inverse(root.left)
		return root
	return recurse_inverse(tree)

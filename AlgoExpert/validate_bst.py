from collections import deque
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
	if tree is None:
		return True
	min_value = float("-inf")
	max_value = float("inf")
    queue = deque()
    queue.append((tree, min_value, max_value))
	while queue:
		current, min_value, max_value = queue.popleft()
		if current is None:
			continue
		if current.value >= max_value or current.value < min_value:
			return False
		#if current.left is not None and current.left.value >= current.value:
		#	return False
		#if current.right is not None and current.right.value < current.value:
		#	return False
		queue.append((current.left, min_value, current.value))
		queue.append((current.right, current.value, max_value))
	return True

'''
#here's a recursive solution:
from collections import deque

def validateBst(tree):
	if tree is None:
		return True
	min_value = float("-inf")
	max_value = float("inf")
	
	def validate_helper(node, min_val, max_val):
		if node is None:
			return True
		if node.value < min_val or node.value >= max_val:
			return False
		if node.left is not None:
			if not validate_helper(node.left, min_val, node.value):
				return False
		if node.right is not None:
			if not validate_helper(node.right, node.value, max_val):
				return False
		return True
	
	return validate_helper(tree, min_value, max_value)

'''
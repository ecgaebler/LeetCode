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
		if current.value > max_value or current.value <= min_value:
			return False
		#if current.left is not None and current.left.value >= current.value:
		#	return False
		#if current.right is not None and current.right.value < current.value:
		#	return False
		queue.append((current.left, min_value, current.value))
		queue.append((current.right, current.value, max_value))
	return True
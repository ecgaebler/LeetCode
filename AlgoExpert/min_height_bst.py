from collections import deque
def minHeightBst(array):
	root_idx = len(array)//2
	root = BST(array[root_idx])
	#Use a queue to determine what order values are inserted
	queue = deque()
	queue.append((0, root_idx))
	queue.append((root_idx + 1, len(array)))
	
	while queue:
		min_idx, max_idx = queue.popleft()
		if min_idx < max_idx:
            #insert midpoint of subtree as new node
			node_idx = (min_idx + max_idx)//2 
			root.insert(array[node_idx])
            #enqueue new nodes left and right subtrees
			queue.append((min_idx, node_idx))
			queue.append((node_idx + 1, max_idx))
	
	return root


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

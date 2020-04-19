# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self
		while True:
			if value < current_node.value:
				if current_node.left == None:
					current_node.left = BST(value)
					break
				else:
					current_node = current_node.left
			else:
				if current_node.right == None:
					current_node.right = BST(value)
				else:
					current_node = current_node.right
					break
        return self

    def contains(self, value):
		current = self
        while current is not None:
			if current.value > value:
				current = current.left
			elif current.value < value:
				current = current.right
			else:
				return True
		return False

    def remove(self, value, parent = None):
		current = self
		while current is not None:
			if value < current.value:
				parent = current
				current = current.left
			elif value > current.value:
				parent = current
				current = current.right
			else: #value matches current node's value
				if current.left is not None and current.right is not None: #current node has two children
					current.value = current.left.largest_value()
					current.left.remove(current.value, current)
					
				elif parent is None: 
					if current.right is not None: #current only has right child
						current.value = current.right.value
						current.left = current.right.left
						current.right = current.right.right
					elif current.left is not None: #current node only has left child
						current.value = current.left.value
						current.right = current.left.right
						current.left = current.left.left
					else: #single-node tree
						pass

				elif current.right is not None: #current node only has a right child
					if parent.left == current:
						parent.left = current.right
					else:
						parent.right = current.right
						
				elif current.left is not None: #current_node only has a left child
					if parent.left == current:
						parent.left = current.left
					else:
						parent.right = current.left

				break
			return self
		
	def largest_value(self):
		current = self
		while current.right is not None:
			current = current.right
		return current.value
		

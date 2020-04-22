class InorderIterator:
  def __init__(self, root):
    self.stack = []
    if root is not None:
      self.stack.append(root)
      node = root
      while node.left is not None:
        self.stack.append(node.left)
        node = node.left

  def hasNext(self):
    if not self.stack:
      return False
    return True
    
  # getNext returns null if there are no more elements in tree
  def getNext(self):
    if not self.hasNext():
      return None
    current_node = self.stack.pop()
    # If right subtree exists, add its left side to the stack.
    if current_node.right is not None:
      node = current_node.right
      self.stack.append(node)
      while node.left is not None:
        self.stack.append(node.left)
        node = node.left
    return current_node

def inorder_using_iterator(root):
  iter = InorderIterator(root)
  result = ""
  while iter.hasNext():
    ptr = iter.getNext()
    result += str(ptr.data) + " "
  return result
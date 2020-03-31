"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: #edge case where starting node is null
            return None
        stack = deque([node]) #for keeping track of nodes to clone
        clone_dict = {} #map original nodes to cloned nodes
        cloned = set() #for noting which nodes have been cloned and recorded in clone_dict
        
        #traverse graph, cloning nodes as new neighborless nodes
        while stack:
            current_node = stack.popleft()
            cloned.add(current_node)
            for neighbor in current_node.neighbors:
                if neighbor not in cloned: #as long as we haven't cloned it yet...
                    stack.append(neighbor) #add neighbor nodes to stack
            new_node = Node(current_node.val, []) #copy the value (mark neighbors later)
            clone_dict[current_node] = new_node #map original node to its clone
        
        #traverse graph a second time, adding neighborhood
        for original_node in clone_dict:
            cloned_node = clone_dict[original_node] #find node clone
            for neighbor in original_node.neighbors:
                cloned_neighbor = clone_dict[neighbor] #find neighbor clone
                cloned_node.neighbors.append(cloned_neighbor) #add neighbor clone to list
            
        return clone_dict[node]
            
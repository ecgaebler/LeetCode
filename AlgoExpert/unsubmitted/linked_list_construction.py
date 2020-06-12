"""
This class should support the following:
- setting the head and tail of the linked list
- inserting nodes before and after other nodes as well as at given positions
- removing given nodes and removing nodes with given values
- searching for nodes with given values

Example usage:
(Assume the following linked list has already been created)
 ① <—> ② <—> ③ <—> ④ <—> ⑤

setHead(④): # set the existing node with value 4 as the head
 ④ <—> ① <—> ② <—> ③ <—> ⑤

setTail(⑥): # set the existing node with value 6 as the tail
 ④ <—> ① <—> ② <—> ③ <—> ⑤ <—> ⑥

insertBefore(⑥, ③): # move the existing node with value 3 before the existing node with value 6
 ④ <—> ① <—> ② <—> ⑤ <—> ③ <—> ⑥

insertAfter(⑥, ③): # insert a new node with value 3 after the existing node with value 6
 ④ <—> ① <—> ② <—> ⑤ <—> ③ <—> ⑥ <—> ③

insertAtPosition(1, ③): # insert a new node with value 3 in position 1
 ③ <—> ④ <—> ① <—> ② <—> ⑤ <—> ③ <—> ⑥ <—> ③

removeNodesWithValue(3): # remove all nodes with value 3
 ④ <—> ① <—> ② <—> ⑤ <—> ⑥

remove(②):# remove the existing node with value 2
 ④ <—> ① <—> ⑤ <—> ⑥

containsNodeWithValue(5): true
"""


# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if node is self.head:
            return
        if node is self.tail:
            self.tail = self.tail.prev #promote second last node to tail
            self.tail.next = None #set new tail's "next" pointer
        else:
            #make node's neighbors point to each other
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        self.head.prev = node #make current head point to node
        node.next = self.head #make node point to current head
        self.head = node #promote node to new head
		
    def setTail(self, node):
        if node is self.tail:
            return
        if node is self.head:
            self.head = self.head.next #promote second node to head
            self.head.prev = None #set new head's "prev" pointer
        else:
            #make node's neighbors point to each other
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        self.tail.next = node #make surrent tail point to node
        node.prev = self.tail #make node point to current tail
        self.tail = node #promote node to new tail

    def insertBefore(self, node, nodeToInsert):
        #move existing node before another existing node
        if self.tail is nodeToInsert:
            self.tail = nodeToInsert.prev #assign new tail
            self.tail.next = None #point new tail at None
        if node is self.head:
            self.head = nodeToInsert
        temp = node.prev
        node.prev = nodeToInsert
        nodeToInsert.next = node
        nodeToInsert.prev = temp

    def insertAfter(self, node, nodeToInsert):
        #insert new node after an existing node
        #if self.head is nodeToInsert:
        #    self.head = nodeToInsert.next #assign new head
        #    self.head.prev = None
        if node is self.tail:
            self.tail = nodeToInsert
        temp = node.next
        node.next = nodeToInsert
        nodeToInsert.prev = node
        nodeToInsert.next = temp

    def insertAtPosition(self, position, nodeToInsert):
        index = 1
        node = self.head
        while index < position:
            index += 1
            node = node.next
        if not node: #inserted past end of list
            self.tail.next = nodeToInsert
            nodeToInsert.prev = self.tail
            self.tail = nodeToInsert
        elif node is self.head: #inserted at head
            node.prev = nodeToInsert
            nodeToInsert.next = node
            self.head = nodeToInsert
        else:
            temp = node.prev
            nodeToInsert.prev = temp
            nodeToInsert.next = node
            node.prev = nodeToInsert

    def removeNodesWithValue(self, value):
        node = self.head
        while node:
            if node.value == value:
                node = remove(node)
            else:
                node = node.next
        
    def remove(self, node):
        next_node = node.next
        prev_node = node.prev
        if node is self.head:
            self.head = next_node
        if node is self.tail:
            self.tail = prev_node
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        return next_node
        
                
            
        # Write your code here.

    def containsNodeWithValue(self, value):
        # Write your code here.

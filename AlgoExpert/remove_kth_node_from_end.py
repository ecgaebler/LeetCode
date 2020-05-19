# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Determine the length of the list
    length = 0
    node = head
    while node:
        length += 1
        node = node.next
    target_idx = length - k #index of node to remove
    
    if target_idx == 0:
        new_head = head.next
        head.next = None
        return new_head
    #progress through list until you get to node with index == target_idx
    parent = None
    node = head
    node_idx = 0

    while node_idx < target_idx:
        parent = node
        node = node.next
        node_idx += 1

    parent.next = node.next #make parent point past target node
    node.next = None
    return head
'''
node0 = LinkedList(0)
node1 = LinkedList(1)
node0.next = node1
node2 = LinkedList(2)
node1.next = node2
node3 = LinkedList(3)
node2.next = node3
node4 = LinkedList(4)
node3.next = node4
head = removeKthNodeFromEnd(node0, 2)
while head:
    print(f"{head.value}-->")
    head = head.next
'''

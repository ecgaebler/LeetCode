# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = []
        current_node = head
        while current_node != None:
            l.append(current_node)
            current_node = current_node.next
        list_len = len(l)
        if list_len <= 1: #list too small to need any changes
            return
        left_iter = 0 #iterator pointing to left side of list
        right_iter = list_len-1 #iterator pointing to right side
        while(left_iter < right_iter):
            l[left_iter].next = l[right_iter]
            left_iter += 1
            l[right_iter].next = l[left_iter]
            right_iter -= 1
        l[left_iter].next = None
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        dummy = node = ListNode()  # creates a dummy node and a node pointer pointing to it

        while list1 and list2: # as long as there are values in both lists
            if list1.val < list2.val: # if list1 val is less than val 2,
                node.next = list1 # sets next node as list1's value
                list1 = list1.next # next list1
            else:  # does the same thing if val2 is less than val1
                node.next = list2 
                list2 = list2.next
            node = node.next # moves onto next node.

        node.next = list1 or list2 # adds the remaining nodes

        return dummy.next # pointer starts at 0 so you start with next
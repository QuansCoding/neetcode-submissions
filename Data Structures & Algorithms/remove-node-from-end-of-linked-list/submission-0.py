# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # creates a dummy node pointing to head

        left = dummy  # init left pointer at dummy
        right = head  # init right pointer at head (first node)

        while n > 0:  # keeps moving right pointer n times
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next  # left next points to next next

        return dummy.next # returns dummy next (which is the first node)
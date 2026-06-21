# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy, 3, 2, 1. we need to get the n + 1 node from end.
        dummy = ListNode(0, head)
        hi = dummy
        lo = dummy

        for _ in range(n + 1):
            hi = hi.next
        
        while hi:
            lo = lo.next
            hi = hi.next
        
        lo.next = lo.next.next
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        n1 = None
        n2 = head

        while n2:
            temp = n2.next
            n2.next = n1
            n1 = n2
            n2 = temp

        return n1 
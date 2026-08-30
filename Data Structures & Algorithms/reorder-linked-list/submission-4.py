# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        n1 = None
        n2 = slow.next

        slow.next = None

        while n2:
            temp = n2.next
            n2.next = n1
            n1 = n2
            n2 = temp
        
        p1 = head
        p2 = n1

        dummy = ListNode()
        cur = dummy
        while p1 or p2:
            if p1:
                cur.next = p1
                p1 = p1.next
                cur = cur.next
            if p2:
                cur.next = p2
                p2 = p2.next
                cur = cur.next
        
        return None
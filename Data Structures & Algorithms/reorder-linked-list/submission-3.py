# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the linked list into 2: 1 form start and the other one from end.
        # rebuild the list one by one.

        # 0, 1, 2
        

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        pre = None
        cur = slow.next
        slow.next = None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        
        p1 = head
        p2 = pre
        
        dummy = ListNode()
        cur = dummy

        while p1 and p2:
            cur.next = p1
            cur = p1
            p1 = p1.next
            cur.next = p2
            cur = p2
            p2 = p2.next

        cur.next = p1 if p1 else p2
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head

        # 0, 1, 2, 3
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        
        return pre

        # T: O(N), S: O(1)
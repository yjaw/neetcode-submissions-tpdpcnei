# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry != 0:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next

            if l2:
                val2 = l2.val
                l2 = l2.next

            cur_sum = carry + val1 + val2
            cur.next = ListNode(val = cur_sum % 10)
            carry = cur_sum // 10
            cur = cur.next
        
        return dummy.next
            
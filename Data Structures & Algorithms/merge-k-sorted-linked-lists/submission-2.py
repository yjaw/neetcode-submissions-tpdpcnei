# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            l1 = lists[0]
            l2 = lists[1]
            dummy = ListNode()
            cur = dummy
            while l1 or l2:
                if l1 and l2:
                    if l1.val < l2.val:
                        cur.next = l1
                        l1 = l1.next
                    else:
                        cur.next = l2
                        l2 = l2.next
                elif l1:
                    cur.next = l1
                    break
                elif l2:
                    cur.next = l2
                    break
                cur = cur.next
            return dummy.next
        
        n = int(len(lists) / 2)
        left = self.mergeKLists(lists[: n])
        right = self.mergeKLists(lists[n: ])
        return self.mergeKLists([left, right])


        
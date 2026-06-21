# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwo(self, a: ListNode, b: ListNode) -> ListNode:
        if a == None: return b
        if b == None: return a

        dummy = ListNode
        cur = dummy
        while a and b:
            if a.val <= b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next
        cur.next = a if a else b
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        que = deque(lists)
        n = len(que)
        while n > 1:
            cur_que = deque()
            while que:
                a = que.popleft() if que else None
                b = que.popleft() if que else None
                cur_que.append(self.mergeTwo(a, b))
            que = cur_que
            n = len(que)
        
        return que.popleft() if que else None


        
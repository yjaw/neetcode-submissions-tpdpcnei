class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 第一趟：建立 舊節點 -> 新節點 的映射
        old_to_new = {None: None}
        
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next
            
        # 第二趟：直接串接 next 與 random 指標
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new[cur.next]
            old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next
            
        return old_to_new[head]
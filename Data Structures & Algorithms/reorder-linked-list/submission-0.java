/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode pre = null;
        ListNode cur = slow.next;
        slow.next = null;
        while (cur != null) {
            ListNode temp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = temp;
        }

        ListNode dummy = new ListNode();
        ListNode ptr = dummy;
        ListNode n1 = head;
        ListNode n2 = pre;

        while (n1 != null || n2 != null) {
            if (n1 != null && n2 != null) {
                ptr.next = n1;
                ptr = n1;
                n1 = n1.next;
                ptr.next = n2;
                ptr = n2;
                n2 = n2.next;
            }
            else if (n1 == null) {
                ptr.next = n2;
                ptr = n2;
                n2 = n2.next;
            }
            else {
                ptr.next = n1;
                ptr = n1;
                n1 = n1.next;
            }
        }
    }
}

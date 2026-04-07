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
    public ListNode mergeKLists(ListNode[] lists) {
        var nodeList = new ArrayList<ListNode>();
        for (ListNode head: lists) {
            nodeList.add(head);
        }
        while (nodeList.size() > 1) {
            int i = 0;
            var nexNodeList = new ArrayList<ListNode>();
            for (; i < nodeList.size() - 1; i += 2) {
                ListNode dummy = new ListNode();
                ListNode cur = dummy;
                ListNode n1 = nodeList.get(i);
                ListNode n2 = nodeList.get(i + 1);
                while (n1 != null && n2 != null) {
                    if (n1.val < n2.val) {
                        cur.next = n1;
                        n1 = n1.next;
                    }
                    else {
                        cur.next = n2;
                        n2 = n2.next;
                    }
                    cur = cur.next;
                }
                if (n1 != null) cur.next = n1;
                else if (n2 != null) cur.next = n2;
                else cur.next = null;
                nexNodeList.add(dummy.next);
            }
            if (i == nodeList.size() - 1) nexNodeList.add(nodeList.get(i));
            nodeList = nexNodeList;
        }
        if (nodeList.size() > 0) {
            return nodeList.get(0);
        }
        return null;
    }
}

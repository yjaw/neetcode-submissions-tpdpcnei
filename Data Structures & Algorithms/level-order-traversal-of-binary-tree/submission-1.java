/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Deque<TreeNode> nodeQue = new LinkedList<>();
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        nodeQue.offer(root);
        while (!nodeQue.isEmpty()) {
            int len = nodeQue.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < len; i++) {
                TreeNode node = nodeQue.poll();
                level.add(node.val);
                if (node.left != null) nodeQue.offer(node.left);
                if (node.right != null) nodeQue.offer(node.right);
            }
            res.add(level);
        }
        return res;
    }
}

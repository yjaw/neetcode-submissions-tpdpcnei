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
    void dfs(TreeNode node, List<Integer> values) {
        if (node == null) return;
        dfs(node.left, values);
        values.add(node.val);
        dfs(node.right, values);
        return;
    }
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> res = new ArrayList<>();
        dfs(root, res);
        if (res.size() < k) return -1;
        else return res.get(k - 1);
    }
}

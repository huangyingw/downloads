/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
  class Solution {
    private int getBalancedTreeHeight(TreeNode root) {
      if (root == null) {
        return 0;
      }

      int l = getBalancedTreeHeight(root.left);
      int r = getBalancedTreeHeight(root.right);

      if (l >= 0 && r >= 0) {
        if (Math.abs(l - r) <= 1) {
          return Math.max(l, r) + 1;
        }
      }

      return -1;
    }

    public boolean isBalanced(TreeNode root) {
      return getBalancedTreeHeight(root) >= 0;
    }
  }


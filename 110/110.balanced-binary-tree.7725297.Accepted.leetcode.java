class Solution {
    private int getBalancedTreeHeight(TreeNode root) {
      if (root == null) {
        return 0;
      }

      int left = getBalancedTreeHeight(root.left);
      int right = getBalancedTreeHeight(root.right);

      if (left < 0 || right < 0 || Math.abs(left - right) > 1) {
        return -1;
      }

      return Math.max(left, right) + 1;
    }

    public boolean isBalanced(TreeNode root) {
      return getBalancedTreeHeight(root) >= 0;
    }
  }


  public class Solution
  {
    public TreeNode upsideDownBinaryTree(TreeNode root)
    {
      return udtree(root, null);
    }

    TreeNode udtree(TreeNode root, TreeNode parent)
    {
      if (root == null) { return parent; } // base

      TreeNode newRoot = udtree(root.left, root);
      root.left = parent == null ? null : parent.right; // 1st node, both .left .right == null
      root.right = parent;
      return newRoot;
    }
  }


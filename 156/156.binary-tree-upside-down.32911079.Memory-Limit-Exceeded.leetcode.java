  public class Solution
  {
    public TreeNode upsideDownBinaryTree(TreeNode root)
    {
      if (root == null)
      {
        return null;
      }

      ArrayList<TreeNode> res = new ArrayList<TreeNode>();
      res.add(null);
      helper(root, res);
      return res.get(0);
    }

    public TreeNode helper(TreeNode root, ArrayList<TreeNode> res)
    {
      if (root.left == null)
      {
        res.set(0, root);
        return root;
      }

      TreeNode newRoot = helper(root.left, res);
      newRoot.left = root.right;
      newRoot.right = root;
      return newRoot.right;
    }
  }


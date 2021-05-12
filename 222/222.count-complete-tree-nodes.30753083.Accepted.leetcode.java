  public class Solution
  {
    public int countNodes(TreeNode root)
    {
      if (root == null)
      {
        return 0;
      }

      int leftHeight = 0, rightHeight = 0;
      TreeNode left = root;
      TreeNode right = root;

      while (left != null)
      {
        left = left.left;
        leftHeight++ ;
      }

      while (right != null)
      {
        right = right.right;
        rightHeight++ ;
      }

      if (leftHeight == rightHeight)
      {
        return (1 << leftHeight) - 1;
      }

      return 1 + countNodes(root.left) + countNodes(root.right);
    }
  }


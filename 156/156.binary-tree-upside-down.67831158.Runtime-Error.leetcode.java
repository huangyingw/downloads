  public class Solution
  {
    public TreeNode upsideDownBinaryTree(TreeNode root)
    {
      TreeNode navNode = root, parentNode = null, leftNode = null,
               rightNode = null;

      while (navNode != null)
      {
        leftNode = navNode.left;
        rightNode = navNode.right;
        navNode.left = null;
        navNode.right = null;
        parentNode = navNode;
        navNode = leftNode;
        leftNode = navNode.left;
        navNode.left = rightNode;
        navNode.right = parentNode;
      }

      return parentNode;
    }
  }


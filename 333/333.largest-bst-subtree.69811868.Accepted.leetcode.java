  public class Solution
  {
    private int res = 0;
    public int largestBSTSubtree(TreeNode root)
    {
      largestBSTHelper(root);
      return res;
    }
    private Data largestBSTHelper(TreeNode root)
    {
      Data curr = new Data();

      if (root == null)
      {
        curr.isBST = true;
        curr.size = 0;
        return curr;
      }

      Data left = largestBSTHelper(root.left);
      Data right = largestBSTHelper(root.right);
      curr.min = Math.min(root.val, Math.min(right.min, left.min));
      curr.max = Math.max(root.val, Math.max(right.max, left.max));

      if (left.isBST && root.val > left.max && right.isBST
          && root.val < right.min)
      {
        curr.isBST = true;
        curr.size = 1 + left.size + right.size;

        if (curr.size > res)
        {
          res = curr.size;
        }
      }
      else
      {
        curr.size = 0;
      }

      return curr;
    }
  }
  class Data
  {
    boolean isBST = false;
    // the minimum for right sub tree or the maximum for right sub tree
    int min = Integer.MAX_VALUE;
    int max = Integer.MIN_VALUE;
    // if the tree is BST, size is the size of the tree; otherwise zero
    int size;
  }


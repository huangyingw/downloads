  public class Solution
  {
    public int closestValue(TreeNode root, double target)
    {
      int closest = root.val;

      while (root != null)
      {
        closest = Math.abs(closest - target) < Math.abs(root.val - target) ? closest : root.val;
        root = target < root.val ? root.left : root.right;
      }

      return closest;
    }
  }


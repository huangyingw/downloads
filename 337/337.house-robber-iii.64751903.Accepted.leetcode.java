  public class Solution
  {
    public int rob(TreeNode root)
    {
      Map<TreeNode, Integer> max = new HashMap<>();
      Map<TreeNode, Integer> maxWO = new HashMap<>();
      rec(root, max, maxWO);
      return max.get(root);
    }

    private void rec(TreeNode root, Map<TreeNode, Integer> max, Map<TreeNode, Integer> maxWO)
    {
      if (root == null)
      {
        max.put(root, 0);
        maxWO.put(root, 0);
        return;
      }

      rec(root.left, max, maxWO);
      rec(root.right, max, maxWO);
      //without root
      maxWO.put(root, (root.left == null ? 0 : max.get(root.left)) + (root.right == null ? 0 : max.get(root.right)));
      //with root
      int maxW = root.val + (root.left == null ? 0 : maxWO.get(root.left)) + (root.right == null ? 0 : maxWO.get(root.right));
      max.put(root, Math.max(maxW, maxWO.get(root)));
    }
  }


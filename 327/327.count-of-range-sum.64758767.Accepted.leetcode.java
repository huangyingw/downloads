  public class Solution
  {
    private class TreeNode
    {
      long val = 0;
      int count = 1;
      int leftSize = 0;
      int rightSize = 0;
      TreeNode left = null;
      TreeNode right = null;
      public TreeNode(long v)
      {
        this.val = v;
        this.count = 1;
        this.leftSize = 0;
        this.rightSize = 0;
      }
    }

    private TreeNode insert(TreeNode root, long val)
    {
      if (root == null)
      {
        return new TreeNode(val);
      }
      else if (root.val == val)
      {
        root.count++;
      }
      else if (val < root.val)
      {
        root.leftSize++;
        root.left = insert(root.left, val);
      }
      else if (val > root.val)
      {
        root.rightSize++;
        root.right = insert(root.right, val);
      }

      return root;
    }

    private int countSmaller(TreeNode root, long val)
    {
      if (root == null)
      {
        return 0;
      }
      else if (root.val == val)
      {
        return root.leftSize;
      }
      else if (root.val > val)
      {
        return countSmaller(root.left, val);
      }
      else
      {
        return root.leftSize + root.count + countSmaller(root.right, val);
      }
    }

    private int countLarger(TreeNode root, long val)
    {
      if (root == null)
      {
        return 0;
      }
      else if (root.val == val)
      {
        return root.rightSize;
      }
      else if (root.val < val)
      {
        return countLarger(root.right, val);
      }
      else
      {
        return countLarger(root.left, val) + root.count + root.rightSize;
      }
    }

    private int rangeSize(TreeNode root, long lower, long upper)
    {
      int total = root.count + root.leftSize + root.rightSize;
      int smaller = countSmaller(root, lower);    // Exclude everything smaller than lower
      int larger = countLarger(root, upper);      // Exclude everything larger than upper
      return total - smaller - larger;
    }

    public int countRangeSum(int[] nums, int lower, int upper)
    {
      if (nums.length == 0)
      {
        return 0;
      }

      long[] sums = new long[nums.length + 1];

      for (int i = 0; i < nums.length; i++)
      {
        sums[i + 1] = sums[i] + nums[i];
      }

      TreeNode root = new TreeNode(sums[0]);
      int output = 0;

      for (int i = 1; i < sums.length; i++)
      {
        output += rangeSize(root, sums[i] - upper, sums[i] - lower);
        insert(root, sums[i]);
      }

      return output;
    }
  }


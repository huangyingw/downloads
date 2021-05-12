public class NumArray
    {
      class SegmentTreeNode
      {
        int start, end;
        int sum;
        SegmentTreeNode left, right;

        // Constructor
        public SegmentTreeNode(int start, int end)
        {
          this.start = start;
          this.end = end;
          sum = 0;
        }

        public SegmentTreeNode(int start, int end, int sum)
        {
          this.start = start;
          this.end = end;
          this.sum = sum;
        }

      }

      private SegmentTreeNode root;

      public NumArray(int[] nums)
      {
        if (nums == null || nums.length == 0)
        {
          return;
        }

        root = buildSegmentTree(nums, 0, nums.length - 1);
      }

      void update(int i, int val)
      {
        updateHelper(root, i, val);
      }

      private void updateHelper(SegmentTreeNode root, int i, int val)
      {
        if (root == null)
        {
          return;
        }

        int mid = root.start + (root.end - root.start) / 2;

        if (i <= mid)
        {
          updateHelper(root.left, i, val);
        }
        else
        {
          updateHelper(root.right, i, val);
        }

        if (root.start == root.end && root.start == i)
        {
          root.sum = val;
          return;
        }

        root.sum = root.left.sum + root.right.sum;
      }

      public int sumRange(int i, int j)
      {
        return sumRangeHelper(root, i, j);
      }

      private int sumRangeHelper(SegmentTreeNode root, int start, int end)
      {
        if (root == null || end < root.start || start > root.end ||
            start > end)
        {
          return 0;
        }

        if (start <= root.start && end >= root.end)
        {
          return root.sum;
        }

        int mid = root.start + (root.end - root.start) / 2;
        return sumRangeHelper(root.left, start, Math.min(end, mid)) +
               sumRangeHelper(root.right, Math.max(mid + 1, start), end);
      }

      private SegmentTreeNode buildSegmentTree(int[] nums, int start, int end)
      {
        if (nums == null || nums.length == 0 || start > end)
        {
          return null;
        }

        // Start == end
        if (start == end)
        {
          return new SegmentTreeNode(start, end, nums[start]);
        }

        SegmentTreeNode root = new SegmentTreeNode(start, end);
        int mid = start + (end - start) / 2;
        root.left = buildSegmentTree(nums, start, mid);
        root.right = buildSegmentTree(nums, mid + 1, end);
        root.sum = root.left.sum + root.right.sum;
        return root;
      }
    }


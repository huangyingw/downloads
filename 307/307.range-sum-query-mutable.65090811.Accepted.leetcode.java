public class NumArray
    {
      int[] tree;
      int[] nums;

      public NumArray(int[] nums)
      {
        this.nums = nums;
        int sum = 0;
        int lowbit;
        tree = new int[nums.length + 1];

        for (int i = 1; i < tree.length; i++)
        {
          sum = 0;
          lowbit = i & (-i);

          for (int j = i; j > i - lowbit; j--)
          {
            sum += nums[j - 1];
          }

          tree[i] = sum;
        }
      }

      void update(int i, int val)
      {
        int diff = val - nums[i];
        nums[i] = val;
        i++;

        for (; i < tree.length; i += (i & (-i)))
        {
          tree[i] += diff;
        }
      }

      public int sumRange(int i, int j)
      {
        return getSum(j) - getSum(i - 1);
      }

      public int getSum(int i)
      {
        int sum = 0;
        i++;

        while (i > 0)
        {
          sum += tree[i];
          i -= (i & (-i));
        }

        return sum;
      }
    }


  public class Solution
  {
    public int[] maxNumber(int[] nums1, int[] nums2, int k)
    {
      int[] ans = new int[k];

      for (int i = Math.max(k - nums2.length, 0); i <= Math.min(nums1.length, k); i++)
      {
        int[] res1 = get_max_sub_array(nums1, i);
        int[] res2 = get_max_sub_array(nums2, k - i);
        int[] res = new int[k];
        int pos1 = 0, pos2 = 0, tpos = 0;

        while (pos1 < res1.length || pos2 < res2.length)
        {
          res[tpos++] = greater(res1, pos1, res2, pos2) ? res1[pos1++] : res2[pos2++];
        }

        if (!greater(ans, 0, res, 0))
        {
          ans = res;
        }
      }

      return ans;
    }

    public boolean greater(int[] nums1, int start1, int[] nums2, int start2)
    {
      for (; start1 < nums1.length && start2 < nums2.length; start1++, start2++)
      {
        if (nums1[start1] > nums2[start2])
        {
          return true;
        }

        if (nums1[start1] < nums2[start2])
        {
          return false;
        }
      }

      return start1 != nums1.length;
    }

    public int[] get_max_sub_array(int[] nums, int k)
    {
      int[] res = new int[k];
      int len = 0;

      for (int i = 0; i < nums.length; i++)
      {
        while (len > 0 && len + nums.length - i > k && res[len - 1] < nums[i])
        {
          len--;
        }

        if (len < k)
        {
          res[len++] = nums[i];
        }
      }

      return res;
    }
  }


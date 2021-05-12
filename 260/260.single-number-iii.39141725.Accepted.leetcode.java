  public class Solution
  {
    public int[] singleNumber(int[] nums)
    {
      int[] res = new int[2];
      res[0] = 0;
      res[1] = 0;
      int n = 0;

      for (int elem : nums)
      {
        n ^= elem;
      }

      n = n & (~(n - 1));

      for (int elem : nums)
      {
        if ((elem & n) != 0)
        {
          res[0] ^= elem;
        }
        else
        {
          res[1] ^= elem;
        }
      }

      return res;
    }
  }


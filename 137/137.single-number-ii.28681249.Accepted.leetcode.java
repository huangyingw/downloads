  public class Solution
  {
    public int singleNumber(int[] A)
    {
      int res = 0;
      int[] digits = new int[32];

      for (int i = 0; i < 32; i++ )
      {
        for (int j = 0; j < A.length; j++ )
        {
          if (1 == ((A[j] >> i) & 1))
          {
            digits[i] = (digits[i] + 1) % 3;
          }
        }

        res |= (digits[i] << i);
      }

      return res;
    }
  }


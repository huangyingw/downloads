  public class Solution
  {
    public int divide(int dividend, int divisor)
    {
      if (dividend == Integer.MIN_VALUE && divisor == -1)
      {
        return Integer.MAX_VALUE;
      }

      long a = Math.abs((long) dividend);
      long b = Math.abs((long) divisor);
      long result = 0;

      while (a >= b)
      {
        long c = b;

        for (int i = 0; a >= c; ++i, c <<= 1)
        {
          a -= c;
          result += 1 << i;
        }
      }

      return (int)(((dividend ^ divisor) >>> 31 == 1) ? -result : result);
    }
  }


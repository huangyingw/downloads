  public class Solution
  {
    public int reverse(int x)
    {
      boolean isNeg = x < 0 ? true : false;
      x = Math.abs(x);
      int res = 0;

      while (x != 0)
      {
        int digit = x % 10;
        x = x / 10;

        if (res > (Integer.MAX_VALUE - digit) / 10)
        {
          return 0;
        }

        res = res * 10 + digit;
      }
      return isNeg == true ? -res : res ;
    }
  }


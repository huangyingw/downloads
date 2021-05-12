  public class Solution
  {
    public int reverseBits(int n)
    {
      String nStr = Long.toBinaryString(n);
      char[] nChar = nStr.toCharArray();
      int len = nStr.length();
      long x = 0;
      int j = len - 1;

      for (int i = 31; i > -1; i--)
      {
        if (j > -1)
        {
          x = x * 2 + (nChar[j] == '1' ? 1 : 0);
          j--;
        }
        else
        {
          x = x * 2;
        }
      }

      return (int)x;
    }
  }


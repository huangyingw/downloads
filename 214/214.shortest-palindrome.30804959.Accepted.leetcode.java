  public class Solution
  {
    public String shortestPalindrome(String s)
    {
      StringBuilder sb = new StringBuilder(s);
      String str = s + "#" + sb.reverse().toString();
      int j = -1;
      int[] next = new int[str.length()];
      next[0] = -1;

      for (int i = 1; i < str.length(); i++ )
      {
        while (j > -1 && str.charAt(j + 1) != str.charAt(i))
        {
          j = next[j];
        }

        if (str.charAt(j + 1) == str.charAt(i))
        {
          j++ ;
        }

        next[i] = j;
      }

      StringBuilder res = new StringBuilder(s.substring(j + 1));
      res.reverse();
      return res.toString() + s;
    }
  }


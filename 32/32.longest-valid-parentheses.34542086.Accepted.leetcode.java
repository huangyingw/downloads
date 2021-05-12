  public class Solution
  {
    public int longestValidParentheses(String s)
    {
      if (s.length() == 0)
      {
        return 0;
      }

      int maxLen = 0;
      int[] d = new int[s.length()];
      // d[i] means substring starts with i has max valid lenth of d[i]
      d[s.length() - 1] = 0;

      for (int i = s.length() - 2; i >= 0; i--)
      {
        if (s.charAt(i) == ')')
        {
          d[i] = 0;
        }
        else
        {
          int j = (i + 1) + d[i + 1];

          if (j < s.length() && s.charAt(j) == ')')
          {
            d[i] = d[i + 1] + 2; //(()())的外包情况

            if (j + 1 < s.length())
            {
              d[i] += d[j + 1];  //()()的后面还有的情况
            }
          }
        }

        maxLen = Math.max(maxLen, d[i]);
      }

      return maxLen;
    }
  }


  public class Solution
  {
    public void reverseWords(char[] s)
    {
      reverse(s, 0, s.length - 1);

      for (int begin = 0, end = 0; end <= s.length; end++)
      {
        if (end == s.length || s[end] == ' ')
        {
          reverse(s, begin, end - 1);

          while (end < s.length && s[end] == ' ')
          {
            end++;
          }

          begin = end ;
        }
      }
    }

    private void reverse(char[] s, int begin, int end)
    {
      for (; begin < end; begin++ , end--)
      {
        char temp = s[begin];
        s[begin] = s[end];
        s[end] = temp;
      }
    }
  }


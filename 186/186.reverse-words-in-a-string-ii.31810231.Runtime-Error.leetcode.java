  public class Solution
  {
    public void reverseWords(char[] s)
    {
      reverse(s, 0, s.length - 1);

      for (int begin = 0, end = 0; end < s.length; end++)
      {
        if (end == s.length - 1 || s[end + 1] == ' ')
        {
          reverse(s, begin, end - 1);
          begin = end + 2;
        }
      }
    }

    private void reverse(char[] s, int begin, int end)
    {
      for (; begin < end; begin++, end--)
      {
        char temp = s[begin];
        s[begin] = s[end];
        s[end] = s[temp];
      }
    }
  }


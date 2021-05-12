  public class Solution
  {
    public boolean isMatch(String s, String p)
    {
      if (p.length() == 0)
      {
        return s.length() == 0;
      }

      if ('*' == p.charAt(1))
      {
        return (isMatch(s, p.substring(2))
          || ((s.charAt(0) == p.charAt(0) || '.' == p.charAt(0))
            && isMatch(s.substring(1), p)));
      }

      if (s.length() == 0)
      {
        return false;
      }

      return (s.charAt(0) == p.charAt(0) || '.' == p.charAt(0))
        ? isMatch(s.substring(1), p.substring(1)) : false;
    }
  }


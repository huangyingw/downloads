  public class Solution
  {
    public int lengthOfLongestSubstring(String s)
    {
      int[] prevPos = new int[Character.MAX_VALUE + 1];
      Arrays.fill(prevPos, -1);
      int begin = 0;
      int maxLen = 0;

      for (int index = 0; index < s.length(); index++)
      {
        begin = Math.max(begin, prevPos[s.charAt(index)] + 1);
        maxLen = Math.max(maxLen, index - begin + 1);
        prevPos[s.charAt(index)] = index;
      }

      return maxLen;
    }
  }


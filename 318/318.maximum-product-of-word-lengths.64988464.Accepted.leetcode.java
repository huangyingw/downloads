  public class Solution
  {
    public int maxProduct(String[] words)
    {
      int n = words.length;
      int[] elements = new int[n];

      for (int i = 0; i < n; i++)
      {
        for (int j = 0; j < words[i].length(); j++)
        {
          elements[i] |= 1 << (words[i].charAt(j) - 'a');
        }
      }

      int ans = 0;

      for (int i = 0; i < n; i++)
      {
        for (int j = i + 1; j < n; j++)
        {
          if ((elements[i] & elements[j]) == 0)
          {
            ans = Math.max(ans, words[i].length() * words[j].length());
          }
        }
      }

      return ans;
    }
  }


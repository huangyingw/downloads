  public class Solution
  {
    public ArrayList<Integer> grayCode(int n)
    {
      ArrayList<Integer> ans = new ArrayList<Integer>();

      for (int i = 0; i < (1 << n); i++)
      {
        ans.add(i ^ (i >> 1));
      }

      return ans;
    }
  }


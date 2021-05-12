  public class Solution {
    public int singleNumber(int[] A) {
      int ans = 0;

      for (int i : A) {
        ans ^= i;
      }

      return ans;
    }
  }


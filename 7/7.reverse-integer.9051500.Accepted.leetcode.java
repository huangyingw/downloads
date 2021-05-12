public class Solution {
    public int reverse(int x) {
      int r = 0;

      for (; x != 0; x /= 10) {
        r = r * 10 + x % 10;
      }

      return r;
    }
  }


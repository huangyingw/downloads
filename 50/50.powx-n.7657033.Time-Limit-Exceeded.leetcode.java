  public class Solution {
    public double pow(double x, int n) {
      double ans = 1;
      double tmp = x;
      boolean neg = false;

      if (n < 0) {
        neg = true;
        n = -n;
      }

      long bound = n;

      while (bound != 0) {
        long i = 1;

        for (; i * 2 <= bound; i *= 2) {
          tmp = tmp * tmp;
        }

        ans *= tmp;
        tmp = x;
        bound = bound - i;
      }

      if (neg) {
        return 1.0 / ans;
      }

      return ans;
    }
  }


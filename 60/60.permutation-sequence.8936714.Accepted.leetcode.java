  public class Solution {
    private int factorial(int n) {
      int r = 1;

      for (int i = 1; i <= n; i++) {
        r *= i;
      }

      return r;
    }

    public String getPermutation(int n, int k) {
      k--; // 0 based
      ArrayList<Integer> numbers = new ArrayList<Integer>();

      for (int i = 1; i <= n; i++) {
        numbers.add(i);
      }

      StringBuilder ans = new StringBuilder();

      while (numbers.size() > 1) {
        int m = factorial(numbers.size() - 1);
        ans.append(numbers.get(k / m));
        numbers.remove(k / m);
        k = k % m;
      }

      ans.append(numbers.get(0));
      return ans.toString();
    }
  }


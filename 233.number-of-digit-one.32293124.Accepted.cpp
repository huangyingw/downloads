class Solution {
  public:
    int countDigitOne(int n) {
      int counts = 0;
      for (int m = 1000000000; m; m /= 10)
        counts += (n / m + 8) / 10 * m + (n / m % 10 == 1) * (n % m + 1);
      return counts;
    }
};


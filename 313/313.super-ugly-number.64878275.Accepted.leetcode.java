  public class Solution
  {
    public int nthSuperUglyNumber(int n, int[] primes)
    {
      int[] times = new int[primes.length];
      int[] result = new int[n];
      result[0] = 1; // first is 1

      for (int i = 1; i < n; i++)
      {
        int min = Integer.MAX_VALUE;

        for (int j = 0; j < primes.length; j++)
        {
          min = Math.min(min, primes[j] * result[times[j]]);
        }

        result[i] = min;

        for (int j = 0; j < times.length; j++)
        {
          if (result[times[j]] * primes[j] == min)
          {
            times[j]++;
          }
        }
      }

      return result[n - 1];
    }
  }


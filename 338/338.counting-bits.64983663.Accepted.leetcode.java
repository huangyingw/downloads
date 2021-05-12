  public class Solution
  {
    public int[] countBits(int num)
    {
      int[] result = new int[num + 1];

      for (int i = 0; i <= num; i++)
      {
        result[i] = countEach(i);
      }

      return result;
    }

    public int countEach(int num)
    {
      int result = 0;

      while (num != 0)
      {
        if (num % 2 == 1)
        {
          result++;
        }

        num = num / 2;
      }

      return result;
    }
  }


  public class Solution
  {
    public int singleNumber(int[] A)
    {
      if (A.length <= 0)
      {
        return -1;
      }

      if (A.length == 1)
      {
        return A[0];
      }

      Arrays.sort(A);
      int j = 1;

      for (int i = 0; i < A.length - 1; i++)
      {
        if (A[i] == A[i + 1])
        {
          j++ ;
        }
        else
        {
          if (j < 3)
          {
            return A[i];
          }

          j = 1;
        }
      }

      return A[A.length - 1];
    }
  }


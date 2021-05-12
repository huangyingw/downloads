public class Solution {
    public int removeDuplicates(int[] A) {
      int distinctCount = 0;

      for (int i = 0; i < A.length; i++)
        if (distinctCount < 2 || A[i] != A[distinctCount - 1]
            || A[i] != A[distinctCount - 2]) {
          A[distinctCount++] = A[i];
        }

      return distinctCount;
    }
  }


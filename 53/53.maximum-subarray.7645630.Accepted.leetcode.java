  public class Solution {
    public int maxSubArray(int[] A) {
      int sum = A[0];
      int maxSum = A[0];

      for (int i = 1; i < A.length; i++) {
        sum = Math.max(sum + A[i], A[i]);
        maxSum = Math.max(maxSum, sum);
      }

      return maxSum;
    }
  }


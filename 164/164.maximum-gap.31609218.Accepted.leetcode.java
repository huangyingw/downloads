  public class Solution
  {
    public int maximumGap(int[] num)
    {
      if (num == null || num.length < 2)
      {
        return 0;
      }

      // get the max and min value of the array
      int min = num[0];
      int max = num[0];

      for (int i : num)
      {
        min = Math.min(min, i);
        max = Math.max(max, i);
      }

      // the minimum possibale len, ceiling of the integer division
      int len = (int) Math.ceil((double)(max - min) / (num.length - 1));
      int[] bucketsMIN = new int[num.length - 1]; // store the min value in that bucket
      int[] bucketsMAX = new int[num.length - 1]; // store the max value in that bucket
      Arrays.fill(bucketsMIN, Integer.MAX_VALUE);
      Arrays.fill(bucketsMAX, Integer.MIN_VALUE);

      // put numbers into buckets
      for (int i : num)
      {
        if (i == min || i == max)
        {
          continue;
        }

        int idx = (i - min) / len; // index of the right position in the buckets
        bucketsMIN[idx] = Math.min(i, bucketsMIN[idx]);
        bucketsMAX[idx] = Math.max(i, bucketsMAX[idx]);
      }

      // scan the buckets for the max len
      int maxGap = Integer.MIN_VALUE;
      int previousMax = min;

      for (int i = 0; i < num.length - 1; i++)
      {
        // empty bucket
        if (bucketsMIN[i] == Integer.MAX_VALUE && bucketsMAX[i] == Integer.MIN_VALUE)
        {
          continue;
        }

        // min value minus the previousMax value is the current maxGap
        maxGap = Math.max(maxGap, bucketsMIN[i] - previousMax);
        // update previousMax bucket value
        previousMax = bucketsMAX[i];
      }

      maxGap = Math.max(maxGap, max - previousMax); // updata the final max value len
      return maxGap;
    }
  }


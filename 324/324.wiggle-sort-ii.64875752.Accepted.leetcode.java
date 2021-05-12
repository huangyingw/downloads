  public class Solution
  {
    public void wiggleSort(int [] nums)
    {
      if (nums.length < 2)
      {
        return;
      }

      int cntForMedian = (nums.length + 1) / 2;
      int median = findKthSmallest(nums, cntForMedian, 0, nums.length - 1);
      mapSortedArrayToWiggleInPlace(nums, median);
    }

    private void mapSortedArrayToWiggleInPlace(int[] nums, int median)
    {
      int i  = 1;
      int begin = 1;
      int end = nums.length;
      int n = nums.length;

      while (i <= end)
      {
        int Ai = indexMap(n, i);

        if (nums[Ai] > median)
        {
          swap(nums, Ai, indexMap(n, begin++));
          i ++;
        }
        else if (nums[Ai] < median)
        {
          swap(nums, Ai, indexMap(n, end--));
        }
        else
        {
          i++;
        }
      }
    }

    private int indexMap(int n, int i)
    {
      return (2 * i - 1) % (n | 1);
    }

    private int findKthSmallest(int [] nums, int k, int start, int end)
    {
      int len = nums.length;

      if (len < 1)
      {
        return 0;
      }

      int left = start;
      int right = end;
      int pivot = nums[end];

      while (true)
      {
        while (left < right && nums[left] < pivot)
        {
          left ++;
        }

        while (left < right && nums[right] >= pivot)
        {
          right --;
        }

        if (left >= right)
        {
          break;
        }

        swap(nums, left, right);
      }

      swap(nums, left, end);

      if (k > left - start + 1)
      {
        return findKthSmallest(nums, k - (left - start + 1), left + 1, end);
      }
      else if (k == left - start + 1)
      {
        return nums[left];
      }
      else
      {
        return findKthSmallest(nums, k, start, left - 1);
      }
    }

    private void swap(int []nums, int start, int end)
    {
      int temp = nums[start];
      nums[start] = nums[end];
      nums[end] = temp;
    }
  }


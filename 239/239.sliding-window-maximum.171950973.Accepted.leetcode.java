public class Solution
{
    public int[] maxSlidingWindow(int[] nums, int k)
    {
        if (nums == null || nums.length == 0)
        {
            return nums;
        }

        k = Math.min(nums.length, k);
        int[] result = new int[nums.length - k + 1];
        Deque<Integer> dequeue = new ArrayDeque<>();

        for (int i = 0; i < nums.length; i++)
        {
            while (!dequeue.isEmpty() && nums[dequeue.getLast()] <= nums[i])
            {
                dequeue.removeLast();
            }

            dequeue.addLast(i);

            while (dequeue.getLast() - dequeue.getFirst() + 1 > k)
            {
                dequeue.removeFirst();
            }

            if (i >= k - 1)
            {
                result[i - (k - 1)] = nums[dequeue.getFirst()];
            }
        }

        return result;
    }
}


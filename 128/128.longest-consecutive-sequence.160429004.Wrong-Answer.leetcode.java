public class Solution
{
    public int longestConsecutive(int[] nums)
    {
        int result = 1;
        Set<Integer> dict = new HashSet<Integer>();

        for (int num : nums)
        {
            dict.add(num);
        }

        for (int num : nums)
        {
            int count = 0;

            if (dict.contains(num))
            {
                int right = num + 1;

                while (dict.contains(right))
                {
                    ++count;
                    dict.remove(right++);
                }

                int left = num - 1;

                while (dict.contains(left))
                {
                    ++count;
                    dict.remove(left--);
                }

                dict.remove(num);
            }

            result = Math.max(result, count);
        }

        return result;
    }
}


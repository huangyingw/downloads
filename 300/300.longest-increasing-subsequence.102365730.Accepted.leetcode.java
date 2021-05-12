public class Solution
{
    public int lengthOfLIS(int[] nums)
    {
        if (nums == null || nums.length == 0)
        {
            return 0;
        }

        ArrayList<Integer> list = new ArrayList<Integer>();

        for (int num : nums)
        {
            if (list.size() == 0)
            {
                list.add(num);
            }
            else if (num > list.get(list.size() - 1))
            {
                list.add(num);
            }
            else
            {
                int i = 0;
                int j = list.size() - 1;

                while (i < j)
                {
                    int mid = (i + j) / 2;

                    if (list.get(mid) < num)
                    {
                        i = mid + 1;
                    }
                    else
                    {
                        j = mid;
                    }
                }

                list.set(j, num);
            }
        }

        return list.size();
    }
}

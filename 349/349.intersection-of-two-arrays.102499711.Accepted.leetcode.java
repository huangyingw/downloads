public class Solution
{
    public int[] intersection(int[] nums1, int[] nums2)
    {
        HashSet<Integer> set1 = new HashSet<Integer>();

        for (int i : nums1)
        {
            set1.add(i);
        }

        HashSet<Integer> set2 = new HashSet<Integer>();

        for (int i : nums2)
        {
            set2.add(i);
        }

        Iterator<Integer> iter = set1.iterator();

        while (iter.hasNext())
        {
            int i = iter.next();

            if (!set2.contains(i))
            {
                iter.remove();
            }
        }

        int[] result = new int[set1.size()];
        int i = 0;

        for (int x : set1)
        {
            result[i++] = x;
        }

        return result;
    }
}

public class Solution
{
    public List<List<Integer>> getFactors(int n)
    {
        List<List<Integer>> ret = new ArrayList<List<Integer>> ();
        helper(ret, new ArrayList<Integer> (), n, 2);
        return ret;
    }

    private void helper(List<List<Integer>> ret, List<Integer> item, int n, int start)
    {
        if (n == 1)
        {
            if (item.size() > 1)
            {
                ret.add(new ArrayList<Integer> (item));
            }
        }

        for (int i = start; i <= n; i++)
        {
            if (n % i == 0)
            {
                item.add(i);
                helper(ret, item, n / i, i);
                item.remove(item.size() - 1);
            }
        }
    }
}

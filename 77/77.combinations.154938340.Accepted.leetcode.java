public class Solution
{
    public List<List<Integer>> combine(int n, int k)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> current = new ArrayList<Integer>();
        helper(1, n, k, result, current);
        return result;
    }
    public void helper(int left, int right, int k, List<List<Integer>> result, List<Integer> current)
    {
        if (k == 0)
        {
            result.add(new ArrayList<Integer>(current));
            return;
        }

        if (left > right)
        {
            return;
        }

        for (int index = left; index <= right; index++)
        {
            current.add(index);
            helper(index + 1, right, k - 1, result, current);
            current.remove(current.size() - 1);
        }
    }
}


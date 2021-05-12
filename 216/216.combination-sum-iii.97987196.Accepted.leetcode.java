public class Solution
{
    public List<List<Integer>> combinationSum3(int k, int n)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        dfs(result, 1, k, n, new ArrayList<Integer>());
        return result;
    }

    private void dfs(List<List<Integer>> result, int start, int k, int n, List<Integer> current)
    {
        if (n < 0 || k < 0)
        {
            return;
        }

        if (k == 0 && n == 0)
        {
            result.add(new ArrayList<Integer>(current));
            return;
        }

        for (int index = start; index <= 9; index++)
        {
            current.add(index);
            dfs(result, index + 1, k - 1, n - index, current);
            current.remove(current.size() - 1);
        }
    }
}

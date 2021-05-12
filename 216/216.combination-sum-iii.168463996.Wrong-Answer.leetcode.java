public class Solution
{
    public List<List<Integer>> combinationSum3(int k, int n)
    {
        List<List<Integer>> re = new ArrayList<List<Integer>>();
        dfs(re, 1, 0, k, n, new ArrayList<Integer>());
        return re;
    }

    private void dfs(List<List<Integer>> result, int start, int target, int k,
                     int n, List<Integer> current)
    {
        if (target < 0 || k < 0)
        {
            return;
        }

        if (k == 0 && target == 0)
        {
            result.add(new ArrayList<Integer>(current));
            return;
        }

        for (int index = start; index <= 9; index++)
        {
            current.add(index);
            dfs(result, index + 1, target - index, k - 1, n, current);
            current.remove(current.size() - 1);
        }
    }
}


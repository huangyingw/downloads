public class Solution
{
    public List<List<Integer>> combinationSum(int[] num, int target)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Arrays.sort(num);
        dfs(num, 0, target, new ArrayList<Integer>(), result);
        return result;
    }
    private void dfs(int[] num, int start, int target, ArrayList<Integer> current, List<List<Integer>> result)
    {
        if (target == 0)
        {
            result.add(new ArrayList<Integer>(current));
            return;
        }

        if (target < 0)
        {
            return;
        }

        for (int index = start; index < num.length; index++)
        {
            current.add(num[index]);
            dfs(num, index, target - num[index], current, result);
            current.remove(current.size() - 1);
        }
    }
}


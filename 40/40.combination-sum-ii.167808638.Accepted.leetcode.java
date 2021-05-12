public class Solution
{
    public List<List<Integer>> combinationSum2(int[] num, int target)
    {
        Arrays.sort(num);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
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

        if (target < 0 || start >= num.length)
        {
            return;
        }

        for (int index = start; index < num.length; index++)
        {
            if (index - 1 >= start && num[index] == num[index - 1])
            {
                continue;
            }

            current.add(num[index]);
            dfs(num, index + 1, target - num[index], current, result);
            current.remove(current.size() - 1);
        }
    }
}


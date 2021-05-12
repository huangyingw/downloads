public class Solution
{
    public List<List<Integer>> combinationSum2(int[] num, int target)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();

        if (num == null || num.length == 0)
        {
            return result;
        }

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

        if (target < 0 || start >= num.length)
        {
            return;
        }

        for (int index = start; index < num.length; index++)
        {
            if (index + 1 < num.length && num[index] == num[index + 1])
            {
                continue;
            }

            current.add(num[index]);
            System.out.printf("current --> %s\n", current);
            dfs(num, index + 1, target - num[index], current, result);
            current.remove(current.size() - 1);
        }
    }
}


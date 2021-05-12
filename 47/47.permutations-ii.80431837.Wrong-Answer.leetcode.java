public class Solution
{
    public List<List<Integer>> permuteUnique(int[] num)
    {
        if (num == null)
        {
            return null;
        }

        List<List<Integer>> result = new ArrayList<List<Integer>>();

        if (num.length == 0)
        {
            return result;
        }

        Arrays.sort(num);
        dfs(num, new ArrayList<Integer>(), result);
        return result;
    }

    private void dfs(int[] num, ArrayList<Integer> current, List<List<Integer>> result)
    {
        if (current.size() == num.length)
        {
            result.add(new ArrayList<Integer>(current));
            return;
        }

        for (int i = 0; i < num.length; i++)
        {
            if (i > 0 && num[i] == num[i - 1])
            {
                continue;
            }

            current.add(num[i]);
            dfs(num, current, result);
            current.remove(current.size() - 1);
        }
    }
}

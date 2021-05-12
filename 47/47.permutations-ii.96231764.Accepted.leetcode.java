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
        dfs(num, new boolean[num.length], new ArrayList<Integer>(), result);
        return result;
    }

    private void dfs(int[] num, boolean[] visited, ArrayList<Integer> current, List<List<Integer>> result)
    {
        if (current.size() == num.length)
        {
            result.add(new ArrayList<Integer>(current));
            return;
        }

        for (int i = 0; i < num.length; i++)
        {
            if (i > 0 && visited[i - 1] && num[i] == num[i - 1])
            {
                continue;
            }

            if (visited[i])
            {
                continue;    
            }
            
            current.add(num[i]);
            visited[i] = true;
            dfs(num, visited, current, result);
            current.remove(current.size() - 1);
            visited[i] = false;
        }
    }
}

public class Solution
{
    public List<List<Integer>> subsets(int[] S)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        dfs(S, 0, new ArrayList<Integer>(), result);
        return result;
    }

    public void dfs(int[] S, int start, List<Integer> current, List<List<Integer>> result)
    {
        result.add(new ArrayList<Integer>(current));
        
        for (int i = start; i < S.length; i++)
        {
            current.add(S[i]);
            dfs(S, i, current, result);
            current.remove(current.size() - 1);
        }
    }
}

public class Solution
{
    public List<List<Integer>> subsetsWithDup(int[] S)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();

        if (S == null)
        {
            return result;
        }

        Arrays.sort(S);
        dfs(S, 0, new ArrayList<Integer>(), result);
        return result;
    }
    public void dfs(int[] S, int start, List<Integer> current,
                    List<List<Integer>> result)
    {
        result.add(new ArrayList<Integer>(current));

        for (int index = start; index < S.length; index++)
        {
            if(index > start && S[index] == S[index-1])
            {
                continue;
            }

            current.add(S[index]);
            dfs(S, index + 1, current, result);
            current.remove(current.size() - 1);
        }
    }
}


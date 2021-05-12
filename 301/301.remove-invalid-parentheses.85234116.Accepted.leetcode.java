public class Solution
{
    private List<String> res = new ArrayList<String>();
    private int max = 0;
    public List<String> removeInvalidParentheses(String s)
    {
        dfs(s, "", 0, 0);

        if (res.size() == 0)
        {
            res.add("");
        }

        return res;
    }

    private void dfs(String str, String subRes, int countLeft, int maxLeft)
    {
        if (str.length() == 0)
        {
            if (countLeft == 0 && subRes.length() != 0)
            {
                if (maxLeft > max)
                {
                    max = maxLeft;
                }

                if (max == maxLeft && !res.contains(subRes))
                {
                    res.add(subRes.toString());
                }
            }

            return;
        }

        if (str.charAt(0) == '(')
        {
            dfs(str.substring(1), subRes.concat("("), countLeft + 1, maxLeft + 1);
            dfs(str.substring(1), subRes, countLeft, maxLeft);
        }
        else if (str.charAt(0) == ')')
        {
            if (countLeft > 0)
            {
                dfs(str.substring(1), subRes.concat(")"), countLeft - 1, maxLeft);
            }

            dfs(str.substring(1), subRes, countLeft, maxLeft);
        }
        else
        {
            dfs(str.substring(1), subRes.concat(String.valueOf(str.charAt(0))), countLeft, maxLeft);
        }
    }
}

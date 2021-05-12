public class Solution
{
    public ArrayList<String> letterCombinations(String digits)
    {
        String[] dic = { " ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
        ArrayList<String> result = new ArrayList<String>();

        if (digits == null || digits.length() == 0)
        {
            return result;
        }

        StringBuilder current = new StringBuilder();
        dfs(digits, dic, current, result);
        return result;
    }

    public void dfs(String digits, String[] dic, StringBuilder current, ArrayList<String> result)
    {
        if (current.length() == digits.length())
        {
            result.add(current.toString());
            return;
        }

        String dicStr = dic[digits.charAt(current.length()) - '0'];

        for (int i = 0; i < dicStr.length(); i++)
        {
            current.append(dicStr.charAt(i));
            dfs(digits, dic, current, result);
            current.deleteCharAt(current.length() - 1);
        }
    }
}


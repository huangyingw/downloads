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

        result.add("");

        if (digits == null || digits.length() == 0)
        {
            return result;
        }

        for (int i = 0; i < digits.length(); i++)
        {
            String letters = dic[digits.charAt(i) - '0'];
            ArrayList<String> newRes = new ArrayList<String>();

            for (int j = 0; j < result.size(); j++)
            {
                for (int k = 0; k < letters.length(); k++)
                {
                    newRes.add(result.get(j) + Character.toString(letters.charAt(k)));
                }
            }

            result = newRes;
        }

        return result;
    }
}


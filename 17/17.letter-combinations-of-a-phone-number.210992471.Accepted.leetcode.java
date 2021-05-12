public class Solution
{
    public List<String> letterCombinations(String digits)
    {
        String[] dic = { " ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
        List<String> result = new LinkedList<>();

        if (digits == null || digits.length() == 0)
        {
            return result;
        }

        LinkedList<String> list = new LinkedList<>();
        list.add("");

        for (int i = 0; i < digits.length(); i++)
        {
            int num = digits.charAt(i) - '0';
            int size = list.size();

            for (int k = 0; k < size; k++)
            {
                String tmp = list.pop();

                for (int j = 0; j < dic[num].length(); j++)
                {
                    list.add(tmp + dic[num].charAt(j));
                }
            }
        }

        result.addAll(list);
        return result;
    }
}


public class Solution
{
    public List<Integer> diffWaysToCompute(String input)
    {
        List<Integer> result = new ArrayList<Integer>();

        for (int i = 0; i < input.length(); i++)
        {
            char ch = input.charAt(i);

            if (ch == '+' || ch == '-' || ch == '*')
            {
                List<Integer> left = diffWaysToCompute(input.substring(0, i));
                List<Integer> right = diffWaysToCompute(input.substring(i + 1, input.length()));

                for (int l : left)
                {
                    for (int r : right)
                    {
                        switch (ch)
                        {
                        case '+' :
                            result.add(l + r);
                            break;

                        case '-' :
                            result.add(l - r);
                            break;

                        case '*' :
                            result.add(l * r);
                            break;
                        }
                    }
                }
            }
        }

        if (result.size() == 0)
        {
            result.add(Integer.valueOf(input));
        }

        return result;
    }
}


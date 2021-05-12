public class Solution
{
    public int calculate(String s)
    {
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(1);
        stack.push(1);
        int result = 0;

        for (int index = 0; index < s.length(); index++)
        {
            char c = s.charAt(index);

            if (Character.isDigit(c))
            {
                int num = c - '0';

                while (index + 1 < s.length() && Character.isDigit(s.charAt(index + 1)))
                {
                    int newNum = s.charAt(index + 1) - '0';
                    num = 10 * num + newNum;
                    index++;
                }

                result += stack.pop() * num;
            }
            else if (c == '+' || c == '(')
            {
                stack.push(stack.peek());
            }
            else if (c == '-')
            {
                stack.push(-1 * stack.peek());
            }
            else if (c == ')')
            {
                stack.pop();
            }
        }

        return result;
    }
}


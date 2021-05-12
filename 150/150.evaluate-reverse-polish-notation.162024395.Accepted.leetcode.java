public class Solution
{
    public int evalRPN(String[] tokens)
    {
        String operators = "+-*/";
        Stack<Integer> stack = new Stack<Integer>();

        for (String token : tokens)
        {
            if (!operators.contains(token))
            {
                stack.push(Integer.parseInt(token));
            }
            else
            {
                int a = stack.pop();
                int b = stack.pop();

                switch (token)
                {
                case "+":
                    stack.push(a + b);
                    break;

                case "-":
                    stack.push(b - a);
                    break;

                case "*":
                    stack.push(a * b);
                    break;

                case "/":
                    stack.push(b / a);
                    break;
                }
            }
        }

        return stack.pop();
    }
}


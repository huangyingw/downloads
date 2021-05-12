public class Solution 
{
    public String parseTernary(String expression) 
    {
        if (expression == null || expression.length() == 0)
        {
            return "";
        }
    
        Stack<Character> stack = new Stack<>();
        char first, second;
        
        for (int i = expression.length() - 1; i >= 0; i--) 
        {
            char c = expression.charAt(i);
            
            if ('0' <= c && c <= '9')
            {
                stack.push(c);
            }
            else if (c == '?')
            {
                first = stack.pop();
                second = stack.pop();
                    
                if (expression.charAt(i + 1) == 'T')
                {
                    stack.push(first);
                }
                else
                {
                    stack.push(second);
                }
            }
            else
            {
                continue;
            }
        }
        
        return String.valueOf(stack.pop());
    }
}

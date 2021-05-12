public class Solution 
{
    public String parseTernary(String expression) 
    {
        if (expression == null || expression.length() == 0)
        {
            return "";
        }
    
        Stack<Character> stack = new Stack<>();
        
        for (int i = expression.length() - 1; i >= 0; i--) 
        {
            char c = expression.charAt(i);
        
            if (!stack.isEmpty() && stack.peek() == '?') 
            {
                stack.pop(); //pop '?'
                char first = stack.pop();
                stack.pop(); //pop ':'
                char second = stack.pop();
         
                if (c == 'T')
                {
                    System.out.println("push first --> " + first);
                    stack.push(first);    
                }
                else
                {
                    System.out.println("push second --> " + second);
                    stack.push(second);    
                }
                
            }
            else 
            {
                System.out.println("push c --> " + c);
                stack.push(c);
            }
        }
    
        return String.valueOf(stack.peek());
    }
}

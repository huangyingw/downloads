public class Solution 
{
    public String removeDuplicateLetters(String s) 
    {
        Map<Character, Integer> counts = new HashMap<Character, Integer>();
        char[] chs = s.toCharArray();
        
        for (char c : s.toCharArray())
        {
            if (counts.get(c) == null)
            {
                counts.put(c, 0);
            }
            
            counts.put(c, counts.get(c) + 1);
        }
        
        Stack<Character> stack = new Stack<Character>();
        
        for (char c : chs)
        {
            if (stack.contains(c))
            {
                counts.put(c, counts.get(c) - 1);
                continue;
            }
            
            while (!stack.isEmpty() && stack.peek() > c && counts.get(stack.peek()) > 1)
            {
                stack.pop();
            }
            
            stack.push(c);
        }
        
        StringBuilder sb = new StringBuilder();
        
        while (!stack.isEmpty())
        {
            sb.append(stack.pop());
        }
        
        return sb.reverse().toString();
    }
}

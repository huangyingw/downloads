  public class Solution
  {
    int longestValidParentheses(String s)
    {
      int result = 0;
      Stack<Integer> stack = new Stack<Integer>();
      char[] charArray = s.toCharArray();

      for (int i = 0; i < charArray.length; i++)
      {
        if (charArray[i] == ')' && !stack.isEmpty()
            && charArray[stack.peek()] == '(')
        {
          stack.pop();

          if (stack.isEmpty())
          {
            result = i + 1;
          }
          else
          {
            result = Math.max(result, i - stack.peek());
          }
        }
        else
        {
          stack.push(i);
        }
      }

      return result;
    }
  }


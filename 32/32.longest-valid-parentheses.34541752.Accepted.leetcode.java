  public class Solution
  {
    int longestValidParentheses(String s)
    {
      int res = 0;
      Stack<Integer> stack = new Stack<Integer>();
      char[] arr = s.toCharArray();

      for (int i = 0; i < arr.length; i++)
      {
        if (arr[i] == ')' && !stack.isEmpty() && arr[stack.peek()] == '(')
        {
          stack.pop();

          if (stack.isEmpty())
          {
            res = i + 1;
          }
          else
          {
            res = Math.max(res, i - stack.peek());
          }
        }
        else
        {
          stack.push(i);
        }
      }

      return res;
    }
  }


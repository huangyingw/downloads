public class Solution
{
    public String simplifyPath(String path)
    {
        String[] splits = path.split("/");
        Stack<String> stack = new Stack<String>();

        for (String split : splits)
        {
            if (split.equals(".."))
            {
                if (!stack.isEmpty())
                {
                    stack.pop();
                }
            }
            else if (split.equals("."))
            {
                continue;
            }
            else
            {
                stack.push(split);
            }
        }

        StringBuilder newPath = new StringBuilder();

        for (String s : stack)
        {
            newPath.append('/');
            newPath.append(s);
        }

        return newPath.length() == 0 ? "/" : newPath.toString();
    }
}

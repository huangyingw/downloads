public class Solution
{
    public String reverseWords(String s)
    {
        StringBuilder sb = new StringBuilder(s.trim().replaceAll(" +", " "));
        reverse(sb, 0, sb.length() - 1);

        for (int begin = 0, end = 0; end <= sb.length(); end++)
        {
            if (sb.charAt(end) == ' ' || end == sb.length())
            {
                reverse(sb, begin, end);
                begin = end + 1;
            }
        }

        return sb.toString();
    }

    public void reverse(StringBuilder sb, int begin, int end)
    {
        for (; begin < end; begin++, end--)
        {
            char temp = sb.charAt(begin);
            sb.setCharAt(begin, sb.charAt(end));
            sb.setCharAt(end, temp);
        }
    }
}


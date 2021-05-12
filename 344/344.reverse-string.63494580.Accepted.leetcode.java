    public class Solution
    {
        public String reverseString(String s)
        {
            StringBuilder sb = new StringBuilder(s);
            reverse(sb, 0, sb.length() - 1);
            return sb.toString();
        }
        private void reverse(StringBuilder sb, int begin, int end)
        {
            for (; begin < end; begin++ , end-- )
            {
                char temp = sb.charAt(begin);
                sb.setCharAt(begin, sb.charAt(end));
                sb.setCharAt(end, temp);
            }
        }
    }


public class Solution
{
    public String multiply(String num1, String num2)
    {
        String n1 = new StringBuilder(num1).reverse().toString();
        String n2 = new StringBuilder(num2).reverse().toString();
        int[] d = new int[n1.length() + n2.length()];

        for (int i = 0; i < n1.length(); i++)
        {
            for (int j = 0; j < n2.length(); j++)
            {
                d[i + j] += (n1.charAt(i) - '0') * (n2.charAt(j) - '0');
            }
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < d.length; i++)
        {
            int digit = d[i] % 10;
            sb.append(digit);
            
            if (i + 1 < d.length)
            {
                d[i + 1] += d[i] / 10;    
            }
        }
        
        while (sb.length() > 1 && sb.charAt(sb.length() - 1) == '0')
        {
            sb.deleteCharAt(sb.length() - 1);
        }

        return sb.reverse().toString();
    }
}

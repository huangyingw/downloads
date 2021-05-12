public class Solution 
{
    public int[] plusOne(int[] digits) 
    {
        int carry = 1;

        for(int i = digits.length - 1; i >= 0; i--)
        {
            digits[i] += carry;
            carry = digits[i] / 10;
            digits[i] %= 10;
        }
        
        if (carry == 1) 
        {
            int[] re = new int[digits.length + 1];
            System.arraycopy(digits, 0, re, 1, digits.length);
            return re;
        }
        else 
        {
            return digits;
        }
    }
}

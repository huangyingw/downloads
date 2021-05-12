public class Solution
{
    public String fractionToDecimal(int numerator, int denominator)
    {
        long a = numerator, b = denominator;

        if (b == 0)
        {
            throw new IllegalArgumentException("denominator must be positive");
        }

        StringBuffer result = new StringBuffer();

        if (a * b < 0)
        {
            result.append("-");
        }

        a = Math.abs(a);
        b = Math.abs(b);
        result.append(a / b);

        if (a % b != 0)
        {
            result.append(".");
            a = a % b * 10;
            Map<Long, Integer> map = new HashMap<Long, Integer>();

            while (a != 0 && map.containsKey(a) == false)
            {
                result.append(a / b);
                map.put(a, result.length());
                a = a % b * 10;
            }

            if (map.containsKey(a))
            {
                result.insert(map.get(a) - 1, "(");
                result.append(")");
            }
        }

        return result.toString();
    }
}


  public class Solution
  {
    public String fractionToDecimal(int numerator, int denominator)
    {
      long a = numerator, b = denominator;

      if (b == 0)
      {
        throw new IllegalArgumentException("denominator must be positive");
      }

      StringBuffer buf = new StringBuffer();

      if (a * b < 0)
      {
        buf.append("-");
      }

      a = Math.abs(a);
      b = Math.abs(b);
      buf.append(a / b);

      if (a % b != 0)
      {
        buf.append(".");
        a = a % b * 10;
        Map<Long, Integer> map = new HashMap();// map numerator a  its sequence number
        int index = buf.length();

        while (a != 0 && map.containsKey(a) == false)
        {
          buf.append(a / b);
          map.put(a, index++);
          a = a % b * 10;
        }

        if (map.containsKey(a))
        {
          buf.insert(map.get(a), "(");
          buf.append(")");
        }
      }

      return buf.toString();
    }
  }


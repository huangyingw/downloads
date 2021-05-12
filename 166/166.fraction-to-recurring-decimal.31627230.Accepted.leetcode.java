  public class Solution
  {
    public String fractionToDecimal(int numerator, int denominator)
    {
      if (numerator == 0) { return "0"; }

      if (denominator == 0) { return "NaN"; }

      StringBuilder ret = new StringBuilder();
      ret.append(((numerator > 0) ^ (denominator > 0)) ? "-" : "");
      long numer = Math.abs((long)numerator);
      long denomin = Math.abs((long) denominator);
      ret.append(Long.toString(numer / denomin));

      if (numer % denomin == 0)
      {
        return ret.toString();
      }
      else
      {
        ret.append(".");
      }

      HashMap<Long, Integer> map = new HashMap<>();
      Long remain = numer %  denomin;

      while (remain > 0)
      {
        if (map.containsKey(remain))
        {
          ret.insert(map.get(remain), "(");
          ret.append(")");
          break;
        }

        map.put(remain, ret.length());
        remain *= 10;
        ret.append(Long.toString(remain / denomin));
        remain %= denomin;
      }

      return ret.toString();
    }
  }


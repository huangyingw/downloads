  public class Solution
  {
    public  String fractionToDecimal(int numerator, int denominator)
    {
      if (denominator == 0) { return "NaN"; }

      if (numerator == 0) { return "0"; }

      String sign = (numerator >>> 31 ^ denominator >>> 31) == 1 ? "-" : "";
      long a = numerator, b = denominator;
      a = Math.abs(a);
      b = Math.abs(b);
      String part1 = a / b + "";
      long mod = a % b;

      if (mod == 0) { return sign + part1; }

      long remain = mod;
      Set<Long> s = new LinkedHashSet<>();

      while (!s.contains(mod) && mod != 0)
      {
        s.add(mod);
        mod = (mod * 10) % b;
      }

      String part2 = "";
      boolean repeated = false;

      for (long i : s)
      {
        if (i == mod)
        {
          part2 += "(";
          repeated = true;
        }

        part2 += (remain * 10) / b;
        remain = (remain * 10) % b;
      }

      if (repeated)
      {
        part2 += ")";
      }

      return sign + part1 + "." + part2;
    }
  }


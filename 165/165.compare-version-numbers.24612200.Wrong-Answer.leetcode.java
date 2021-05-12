  public class Solution
  {
    int compareVersion(String version1, String version2)
    {
      for (int i1 = 0, i2 = 0; i1 < version1.length() || i2 < version2.length(); i1++ , i2++)
      {
        int num1 = 0;

        while (version1.indexOf(i1) != '.' && i1 < version1.length())
        {
          num1 = num1 * 10 + (version1.indexOf(i1++) - '0');
          int num2 = 0;

          while (version2.indexOf(i2) != '.' && i2 < version2.length())
          {
            num2 = num2 * 10 + (version2.indexOf(i2++) - '0');

            if (num1 > num2)
            {
              return 1;
            }

            if (num1 < num2)
            {
              return -1;
            }
          }

          return 0;
        }
      }

      return 1;
    }
  }


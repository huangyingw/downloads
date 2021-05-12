public class Solution
{
    public int compareVersion(String version1, String version2)
    {
        String[] ver1 = version1.split("\\.");
        String[] ver2 = version2.split("\\.");
        int index1 = 0;
        int index2 = 0;

        while (index1 < ver1.length && index2 < ver2.length)
        {
            if (Integer.parseInt(ver1[index1]) < Integer.parseInt(ver2[index2]))
            {
                return -1;
            }
            else if (Integer.parseInt(ver1[index1]) > Integer.parseInt(ver2[index2]))
            {
                return 1;
            }
            else
            {
                index1++;
                index2++;
            }
        }

        if (ver1.length < ver2.length)
        {
            return  -1;
        }
        else if (ver1.length > ver2.length)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
}


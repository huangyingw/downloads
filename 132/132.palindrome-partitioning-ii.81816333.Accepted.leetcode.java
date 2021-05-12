public class Solution
{
    public int minCut(String s)
    {
        int n = s.length();
        int[] f = new int[n + 1];
        boolean p[][] = new boolean[n][n];

        for (int i = 0; i <= n; i++ )
        {
            f[i] = n - 1 - i;
        }

        for (int i = n - 1; i >= 0; i-- )
        {
            for (int j = i; j < n; j++ )
            {
                if (s.charAt(i) == s.charAt(j) && (j - i < 2 || p[i + 1][j - 1]))
                {
                    p[i][j] = true;
                    f[i] = Math.min(f[i], f[j + 1] + 1);
                }
            }
        }

        return f[0];
    }
}

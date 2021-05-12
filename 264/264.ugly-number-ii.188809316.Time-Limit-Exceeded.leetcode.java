public class Solution
{
    public int nthUglyNumber(int n)
    {
        int[] uglyNumber = new int[n];
        int[] index = new int[3]; // respectively for 2,3,5
        int[] factor = {2, 3, 5}; // respectively for 2,3,5
        uglyNumber[0] = 1;

        for (int i = 1; i < n; i++)
        {
            int min = Math.min(Math.min(factor[0], factor[1]), factor[2]);
            uglyNumber[i] = min;

            if (min == factor[0])
            {
                factor[0] = 2 * uglyNumber[++index[0]];
                System.out.printf("factor[0] --> %s\n", factor[0]) ;
            }

            if (min == factor[1])
            {
                factor[1] = 3 * uglyNumber[++index[1]];
                System.out.printf("factor[1] --> %s\n", factor[1]) ;
            }

            if (min == factor[2])
            {
                factor[2] = 5 * uglyNumber[++index[2]];
                System.out.printf("factor[2] --> %s\n", factor[2]) ;
            }
        }

        return uglyNumber[n - 1];
    }
}


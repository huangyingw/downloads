public class Solution extends Relation
{
    public int findCelebrity(int n)
    {
        if (n == 0)
        {
            return -1;
        }

        int can = 0;

        for (int i = 1; i < n; i ++)
        {
            if (!knows(i, can))
            {
                can = i;
            }
        }

        for (int i = 0; i < n; i ++)
        {
            if (i != can)
            {
                if (!knows(i, can) || knows(can, i))
                {
                    return -1;
                }
            }
        }

        return can;
    }
}

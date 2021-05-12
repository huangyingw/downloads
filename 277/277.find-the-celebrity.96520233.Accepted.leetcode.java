public class Solution extends Relation
{
    public int findCelebrity(int n)
    {
        int[] bitmap = new int[n];

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (i == j)
                {
                    continue;
                }

                if (bitmap[j] >= 0)
                {
                    if (knows(i, j))
                    {
                        bitmap[i] = -1;
                        bitmap[j]++;
                    }
                    else
                    {
                        bitmap[j] = -1;
                    }
                }
            }
        }

        for (int i = 0; i < n; i++)
        {
            if (bitmap[i] == n - 1)
            {
                for (int j = 0; j < n; j++)
                {
                    if (i == j)
                    {
                        continue;
                    }

                    if (knows(i, j))
                    {
                        return -1;
                    }
                }

                return i;
            }
        }

        return -1;
    }
}

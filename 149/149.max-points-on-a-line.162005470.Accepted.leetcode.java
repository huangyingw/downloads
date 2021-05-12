public class Solution
{
    public int maxPoints(Point[] points)
    {
        int res = 0, n = points.length;

        for (int i = 0; i < n; ++i)
        {
            int duplicate = 1;

            for (int j = i + 1; j < n; ++j)
            {
                int cnt = 0;
                long x1 = points[i].x, y1 = points[i].y;
                long x2 = points[j].x, y2 = points[j].y;

                if (x1 == x2 && y1 == y2)
                {
                    ++duplicate;
                    continue;
                }

                for (int k = 0; k < n; ++k)
                {
                    int x3 = points[k].x, y3 = points[k].y;

                    if (x1 * y2 + x2 * y3 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3 == 0)
                    {
                        ++cnt;
                    }
                }

                res = Math.max(res, cnt);
            }

            res = Math.max(res, duplicate);
        }

        return res;
    }
}


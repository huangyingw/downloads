public class Solution
{
    public int maxPoints(Point[] points)
    {
        int res = 0;

        for (int i = 0; i < points.length; ++i)
        {
            Map<Map<Integer, Integer>, Integer> m = new HashMap<>();
            int duplicate = 1;

            for (int j = i + 1; j < points.length; ++j)
            {
                if (points[i].x == points[j].x && points[i].y == points[j].y)
                {
                    ++duplicate; continue;
                }

                int dx = points[j].x - points[i].x;
                int dy = points[j].y - points[i].y;
                int d = gcd(dx, dy);
                Map<Integer, Integer> t = new HashMap<>();
                t.put(dx / d, dy / d);
                m.put(t, m.getOrDefault(t, 0) + 1);
            }

            res = Math.max(res, duplicate);

            for (Map.Entry<Map<Integer, Integer>, Integer> e : m.entrySet())
            {
                res = Math.max(res, e.getValue() + duplicate);
            }
        }

        return res;
    }
    public int gcd(int a, int b)
    {
        return (b == 0) ? a : gcd(b, a % b);
    }
}


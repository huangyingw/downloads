class Line
{
    public double a, b, c;
    public Line(double a, double b, double c)
    {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public Line(int x1, int y1, int x2, int y2)
    {
        if (x1 == x2)
        {
            if (x1 == 0)
            {
                a = 1;
                b = 0;
                c = 0;
            }
            else
            {
                a = 1.0 / x1;
                b = 0;
                c = 1;
            }
        }
        else if (y1 == y2)
        {
            if (y1 == 0)
            {
                a = 0;
                b = 1;
                c = 0;
            }
            else
            {
                a = 0;
                b = 1.0 / y1;
                c = 1;
            }
        }
        else
        {
            if (x1 * y2 == x2 * y1)
            {
                a = 1;
                b = - 1.0 * (y1 - y2) / (x1 - x2);
                c = 0;
            }
            else
            {
                a = 1.0 * (y1 - y2) / (x2 * y1 - x1 * y2);
                b = 1.0 * (x1 - x2) / (x1 * y2 - x2 * y1);
                c = 1;
            }
        }
    }

    public String toString()
    {
        return Double.toString(a) + " " + Double.toString(b) + " " + Double.toString(c);
    }
}

public class Solution
{

    public int maxPoints(Point[] points)
    {
        if (points.length < 2)
        {
            return points.length;
        }

        HashMap<String, Integer> hash = new HashMap<String, Integer>();

        for (int i = 0; i < points.length; i++)
        {
            for (int j = i + 1; j < points.length; j++)
            {
                Line line = new Line(points[i].x, points[i].y,
                                     points[j].x, points[j].y);
                String key = line.toString();

                if (hash.containsKey(key))
                {
                    hash.put(key, hash.get(key) + 1);
                }
                else
                {
                    hash.put(key, 1);
                }
            }
        }

        int max = 0;
        String maxKey = "";

        for (String key : hash.keySet())
        {
            if (hash.get(key) > max)
            {
                max = hash.get(key);
                maxKey = key;
            }
        }

        String[] params = maxKey.split(" ");
        double a = Double.parseDouble(params[0]);
        double b = Double.parseDouble(params[1]);
        double c = Double.parseDouble(params[2]);
        int count = 0;

        for (int i = 0; i < points.length; i++)
        {
            if (Math.abs(a * points[i].x + b * points[i].y - c) < 1e-6)
            {
                count++;
            }
        }

        return count;
    }
}


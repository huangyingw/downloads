public class Solution
{
    public int shortestWordDistance(String[] words, String word1, String word2)
    {
        int p1 = -1, p2 = -1, distance = words.length;

        for (int i = 0; i < words.length; i++)
        {
            if (words[i].equals(word1))
            {
                System.out.printf("p1 --> %s\n", p1);
                p1 = i;
            }

            if (words[i].equals(word2))
            {
                System.out.printf("p2 --> %s\n", p2);
                p2 = i;
            }

            if (p1 != -1 && p2 != -1)
            {
                distance = (p1 != p2) ? Math.min(distance, Math.abs(p1 - p2)) : distance;
                System.out.printf("distance --> %s\n", distance);
            }
        }

        return distance;
    }
}


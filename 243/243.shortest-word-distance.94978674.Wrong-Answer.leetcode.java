public class Solution
{
    public int shortestDistance(String[] words, String word1, String word2)
    {
        int p1 = -1, p2 = -1, distance = Integer.MAX_VALUE;

        for (int i = 0; i < words.length; i++)
        {
            if (words[i].equals(word1))
            {
                p1 = i;
            }

            if (words[i].equals(word2))
            {
                p2 = i;
            }
            
            System.out.println("p1 --> " + p1);
            System.out.println("p2 --> " + p2);
            distance = Math.min(distance, Math.abs(p1 - p2));
        }

        return distance;
    }
}

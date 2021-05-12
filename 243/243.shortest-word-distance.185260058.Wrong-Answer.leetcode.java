public class Solution
{
    public int shortestDistance(String[] words, String word1, String word2)
    {
        int idx1 = -1, idx2 = -1, distance = Integer.MAX_VALUE;

        for (int i = 0; i < words.length; i++)
        {
            if (words[i].equals(word1))
            {
                idx1 = i;
                System.out.printf("idx1 --> %s\n", idx1);
            }

            if (words[i].equals(word2))
            {
                idx2 = i;
                System.out.printf("idx2 --> %s\n", idx2);
            }

            distance = Math.min(distance, Math.abs(idx1 - idx2));
        }

        return distance;
    }
}


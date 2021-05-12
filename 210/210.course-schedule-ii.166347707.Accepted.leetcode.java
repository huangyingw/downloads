public class Solution
{
    public int[] findOrder(int numCourses, int[][] prerequisites)
    {
        int len = prerequisites.length;
        int[] pCounter = new int[numCourses];

        for (int i = 0; i < len; i++)
        {
            pCounter[prerequisites[i][0]]++;
        }

        LinkedList<Integer> queue = new LinkedList<Integer>();

        for (int i = 0; i < numCourses; i++)
        {
            if (pCounter[i] == 0)
            {
                queue.add(i);
            }
        }

        int numNoPre = queue.size();
        int[] result = new int[numCourses];
        int j = 0;

        while (!queue.isEmpty())
        {
            int c = queue.remove();
            result[j++] = c;

            for (int i = 0; i < len; i++)
            {
                if (prerequisites[i][1] == c)
                {
                    pCounter[prerequisites[i][0]]--;

                    if (pCounter[prerequisites[i][0]] == 0)
                    {
                        queue.add(prerequisites[i][0]);
                        numNoPre++;
                    }
                }
            }
        }

        if (numNoPre == numCourses)
        {
            return result;
        }

        return new int[0];
    }
}


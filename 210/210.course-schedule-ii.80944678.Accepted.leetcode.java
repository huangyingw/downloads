public class Solution
{
    public int[] findOrder(int numCourses, int[][] prerequisites)
    {
        List<List<Integer>> adjacencyList = new ArrayList<List<Integer>>();
        int[] in = new int[numCourses];

        for (int i = 0; i < numCourses; i++)
        {
            adjacencyList.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < prerequisites.length; i++)
        {
            adjacencyList.get(prerequisites[i][1]).add(prerequisites[i][0]);
            in[prerequisites[i][0]]++;
        }

        LinkedList<Integer> queue = new LinkedList<Integer>();

        for (int i = 0; i < numCourses; ++i)
        {
            if (in[i] == 0)
            {
                queue.offer(i);
            }
        }

        int[] res = new int[numCourses];
        int index = 0;

        while (!queue.isEmpty())
        {
            int t = queue.pop();
            res[index++] = t;

            for (Integer a : adjacencyList.get(t))
            {
                in[a]--;

                if (in[a] == 0)
                {
                    queue.offer(a);
                }
            }
        }

        if (index == numCourses)
        {
            return res;
        }

        return new int[0];
    }
}

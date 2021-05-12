public class Solution 
{
    public int[][] reconstructQueue(int[][] people) 
    {
        int size = people.length;
        LinkedList<int[]> list = new LinkedList<int[]>();
        
        for (int i = 0; i < size; i++) 
        {
            list.add(new int[]{people[i][0], people[i][1], 0});
        }
        
        int ans[][] = new int[size][];
        for (int i = 0; i < size; i++) 
        {
            Collections.sort(list, new Comparator<int[]>() {
                public int compare (int[] a, int[] b) {
                    if (a[1] == b[1])
                        return a[0] - b[0];
                    return a[1] - b[1];
                }
            });
            int[] head = list.removeFirst();
            ans[i] = new int[]{head[0], head[1] + head[2]};
            
            for (int[] p : list) 
            {
                if (p[0] <= head[0]) 
                {
                    p[1] -= 1;
                    p[2] += 1;
                }
            }
        }
        
        return ans;
    }
}

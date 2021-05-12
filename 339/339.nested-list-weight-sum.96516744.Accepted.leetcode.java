/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class Solution
{
    public int depthSum(List<NestedInteger> nestedList)
    {
        int sum = 0;
        LinkedList<NestedInteger> queue = new LinkedList<NestedInteger>();
        LinkedList<Integer> depth = new LinkedList<Integer>();

        for (NestedInteger ni : nestedList)
        {
            queue.offer(ni);
            depth.offer(1);
        }

        while (!queue.isEmpty())
        {
            NestedInteger top = queue.poll();
            int dep = depth.poll();

            if (top.isInteger())
            {
                sum += dep * top.getInteger();
            }
            else
            {
                for (NestedInteger ni : top.getList())
                {
                    queue.offer(ni);
                    depth.offer(dep + 1);
                }
            }
        }

        return sum;
    }
}

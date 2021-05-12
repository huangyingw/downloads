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
    private int maxDepth(List<NestedInteger> nestedList, int depth)
    {
        int max = depth;

        for (NestedInteger ni : nestedList)
        {
            if (!ni.isInteger())
            {
                max = Math.max(max, maxDepth(ni.getList(), depth + 1));
            }
        }

        return max;
    }
    private int sum(List<NestedInteger> nestedList, int depth)
    {
        int sum = 0;

        for (NestedInteger ni : nestedList)
        {
            if (ni.isInteger())
            {
                sum += ni.getInteger() * depth;
            }
            else
            {
                sum += sum(ni.getList(), depth - 1);
            }
        }

        return sum;
    }
    public int depthSumInverse(List<NestedInteger> nestedList)
    {
        if (nestedList == null || nestedList.isEmpty())
        {
            return 0;
        }

        int max = maxDepth(nestedList, 1);
        return sum(nestedList, max);
    }
}

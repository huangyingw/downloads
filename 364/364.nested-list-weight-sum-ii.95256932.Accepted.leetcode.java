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
    public int depthSumInverse(List<NestedInteger> nestedList)
    {
        if (nestedList == null || nestedList.isEmpty())
        {
            return 0;
        }

        int level = getLv(nestedList);
        int sum = getSum(nestedList, level);
        return sum;
    }

    private int getLv(List<NestedInteger> nestedList)
    {
        if (nestedList == null || nestedList.isEmpty())
        {
            return 0;
        }

        int level = 0;
        boolean hasInt = false;

        for (NestedInteger ni : nestedList)
        {
            if (!ni.isInteger())
            {
                int curLv = getLv(ni.getList());

                if (curLv > level)
                {
                    level = curLv;
                }
            }
            else
            {
                hasInt = true;
            }
        }

        return (level > 0 || hasInt) ? level + 1 : 0;
    }

    private int getSum(List<NestedInteger> nestedList, int level)
    {
        if (level == 0 || nestedList == null || nestedList.isEmpty())
        {
            return 0;
        }

        int sum = 0;

        for (NestedInteger ni : nestedList)
        {
            if (ni.isInteger())
            {
                sum += ni.getInteger() * level;
            }
            else
            {
                sum += getSum(ni.getList(), level - 1);
            }
        }

        return sum;
    }
}

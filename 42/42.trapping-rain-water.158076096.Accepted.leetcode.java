public class Solution
{
    public int trap(int[] heights)
    {
        if (heights.length == 0)
        {
            return 0;
        }

        int[] leftMax = new int[heights.length];
        leftMax[0] = heights[0];

        for (int i = 1; i < heights.length; i++)
        {
            leftMax[i] = Math.max(leftMax[i - 1], heights[i - 1]);
        }

        int rightMax = heights[heights.length - 1], area = 0;

        for (int i = heights.length - 1; i >= 0; i--)
        {
            rightMax = Math.max(rightMax, heights[i]);
            area += Math.max(Math.min(rightMax, leftMax[i]) - heights[i], 0);
        }

        return area;
    }
}


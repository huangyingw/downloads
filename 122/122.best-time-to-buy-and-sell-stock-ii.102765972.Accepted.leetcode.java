public class Solution
{
    public int maxProfit(int[] prices)
    {
        if (prices == null || prices.length < 2)
        {
            return 0;
        }
        
        int profit = 0;

        for (int i = 1; i < prices.length; i++)
        {
            profit += Math.max(0, prices[i] - prices[i - 1]);
        }

        return profit;
    }
}

public class Solution
{
    public int maxProfit(int[] prices)
    {
        int[] preProfit = new int[prices.length];
        preProfit[0] = 0;
        int minPrice = prices[0];

        for (int i = 1; i < prices.length; i++)
        {
            minPrice = Math.min(minPrice, prices[i - 1]);
            preProfit[i] = Math.max(preProfit[i - 1], prices[i] - minPrice);
        }

        int maxPrice = prices[prices.length - 1];
        int maxProfit = preProfit[prices.length - 1];

        for (int i = prices.length - 2; i > 0; i--)
        {
            maxPrice = Math.max(maxPrice, prices[i]);
            maxProfit = Math.max(maxProfit, preProfit[i - 1] + maxPrice - prices[i]);
        }

        return maxProfit;
    }
}


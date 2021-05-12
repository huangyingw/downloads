public class Solution
{
    int canCompleteCircuit(int[] gas, int[] cost)
    {
        int leftGas = 0, sum = 0, startnode = 0;

        for (int i = 0; i < gas.length; ++i)
        {
            leftGas += gas[i] - cost[i];
            sum += gas[i] - cost[i];

            if (sum < 0)
            {
                startnode = i + 1;
                sum = 0;
            }
        }

        return (leftGas < 0) ? -1 : startnode;
    }
}


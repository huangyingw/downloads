public class Solution extends Relation
{
    public int findCelebrity(int n)
    {
        if (n <= 1)
        {
            return 0;
        }

        int left = 0;
        int right = n - 1;

        while (left < right)
        {
            if (knows(left, right))
            {
                left++;
            }
            else
            {
                right--;
            }
        }

        return left;
    }
}

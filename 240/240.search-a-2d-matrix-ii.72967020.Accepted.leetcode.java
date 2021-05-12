public class Solution
{
    public boolean searchMatrix(int[][] matrix, int target)
    {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
        {
            return false;
        }

        int m = matrix.length;
        int n = matrix[0].length;
        int row = m - 1;
        int col = 0;

        while (row >= 0 && row < m && col >= 0 && col < n)
        {
            int cur = matrix[row][col];

            if (cur == target)
            {
                return true;
            }
            else if (cur > target)
            {
                row-- ;
            }
            else
            {
                col++ ;
            }
        }

        return false;
    }
}


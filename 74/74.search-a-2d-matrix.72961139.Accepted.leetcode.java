public class Solution
{
    public boolean searchMatrix(int[][] matrix, int target)
    {
        if (matrix.length == 0 || matrix[0].length == 0)
        {
            return false;
        }

        int columns = matrix[0].length;
        int left = 0;
        int right = matrix.length * columns - 1;

        while (left + 1 < right)
        {
            int mid = left + (right - left) / 2;
            int val = matrix[mid / columns][mid % columns];

            if (val < target)
            {
                left = mid;
            }
            else if (val > target)
            {
                right = mid;
            }
            else
            {
                return true;
            }
        }

        return (matrix[left / columns][left % columns] == target || matrix[right / columns][right % columns] == target);
    }
}


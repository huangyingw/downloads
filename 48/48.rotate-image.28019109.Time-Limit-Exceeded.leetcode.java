public class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for(int i = 1;i < n;i++)
        {
            for(int j = 0;j < i;j++)
            {
                matrix[i][j] ^= matrix[j][i];
                matrix[j][i] ^= matrix[i][j];
                matrix[i][j] ^= matrix[j][i];
            }
        }
        for(int i = 0;i < n;i++)
        {
            int left = 0, right = n - 1;
            while(left < right)
            {
                matrix[i][left] ^= matrix[i][right];
                matrix[i][right] ^= matrix[i][left];
                matrix[i][left] ^= matrix[i][right];
            }
        }
    }
}

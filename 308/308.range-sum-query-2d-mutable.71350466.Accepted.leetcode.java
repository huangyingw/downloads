public class NumMatrix {
    int[][] rowSums;
    
    public NumMatrix(int[][] matrix) {
        if (matrix.length == 0)
            return;
        rowSums = new int[matrix.length][matrix[0].length];
        
        // 建rowSums矩阵
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                rowSums[i][j] = matrix[i][j] + (j == 0 ? 0 : rowSums[i][j - 1]);
            }
        }
    }

    public void update(int row, int col, int val) {
        // 求出新值与旧值的差
        int diff = val - (rowSums[row][col] - (col == 0 ? 0 : rowSums[row][col - 1]));
        
        // 更新该行受影响的sum
        for (int j = col; j < rowSums[0].length; j++) {
            rowSums[row][j] += diff;
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        int res = 0;

        // 逐行求和，每行的相应和为两sum相减
        for (int i = row1; i <= row2; i++) {
            res += rowSums[i][col2] - (col1 == 0 ? 0 :rowSums[i][col1 - 1]);
        }
        return res;
    }
}

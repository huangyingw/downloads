class Solution 
{
    /**
     * Get all distinct N-Queen solutions
     * @param n: The number of queens
     * @return: All distinct solutions
     * For example, A string '...Q' shows a queen on forth position
     */
    List<List<String>> solveNQueens(int n) 
    {
        // write your code here
        List<List<String>> result = new ArrayList<>();
        
        if (n <= 0) 
        {
            return result;
        }
        
        int[] row = new int[n];
        solveNQueensCore(result, row, n, 0);
        return result;
    }
    
    private void solveNQueensCore(List<List<String>> result,
                              int[] row,
                              int n,
                              int index) 
                              {
        if (index == n) 
        {
            result.add(translateString(row));
            return;
        }
        
        for (int i = 0; i < n; i++) 
        {
            if (isValid(row, index, i)) 
            {
                row[index] = i;
                solveNQueensCore(result, row, n, index + 1);
                row[index] = 0;
            }
        }
    }
    
    private ArrayList<String> translateString(int[] row) 
    {
        ArrayList<String> result = new ArrayList<>();
        for (int i = 0; i < row.length; i++) 
        {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < row.length; j++) 
            {
                if (j == row[i]) 
                {
                    sb.append('Q');
                }
                else 
                {
                    sb.append('.');
                }
            }
            
            result.add(sb.toString());
        }
        
        return result;
    }
    
    private boolean isValid(int[] row, int rowNum, int columnNum) 
    {
        for (int i = 0; i < rowNum; i++) 
        {
            if (row[i] == columnNum) 
            {
                return false;
            }
            
            if (Math.abs(row[i] - columnNum) == Math.abs(i - rowNum)) 
            {
                return false;
            }
        }
        
        return true;
    }
    
}

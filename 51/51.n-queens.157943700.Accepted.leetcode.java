public class Solution
{
    public List<List<String>> solveNQueens(int n)
    {
        List<List<String>> result = new ArrayList<List<String>>();
        dfs(n, 0, new int[n], result);
        return result;
    }

    private void dfs(int n, int row, int[] columnForRow, List<List<String>> result)
    {
        if (row == n)
        {
            List<String> strRows = new ArrayList<String>();
            char[] strRow = new char[n];
            Arrays.fill(strRow, '.');

            for (int i = 0; i < n; i++)
            {
                strRow[columnForRow[i]] = 'Q';
                strRows.add(new String(strRow));
                strRow[columnForRow[i]] = '.';
            }

            result.add(strRows);
            return;
        }

        for (int col = 0; col < n; col++)
        {
            if (isValid(n, columnForRow, row, col))
            {
                columnForRow[row] = col;
                dfs(n, row + 1, columnForRow, result);
            }
        }
    }

    private boolean isValid(int n, int[] columnForRow, int row, int col)
    {
        int leftTop = col;
        int rightTop = col;

        for (int i = row - 1; i >= 0; i--)
        {
            leftTop--;
            rightTop++;

            if (columnForRow[i] == col || columnForRow[i] == leftTop || columnForRow[i] == rightTop)
            {
                return false;
            }
        }

        return true;
    }
}


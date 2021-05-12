public class Solution
{
    public List<List<String>> solveNQueens(int n)
    {
        List<List<String>> res = new ArrayList<List<String>>();
        dfs(res, new int[n], 0, n);
        return res;
    }

    public void dfs(List<List<String>> res, int[] usedColumns, int curRow, int total)
    {
        if (curRow == total)
        {
            List<String> board = new ArrayList<String>();

            for (int row = 0; row < total; row++)
            {
                StringBuilder sb = new StringBuilder();

                for (int col = 0; col < total; col++)
                {
                    if (col == usedColumns[row])
                    {
                        sb.append("Q");
                    }
                    else
                    {
                        sb.append(".");
                    }
                }

                board.add(sb.toString());
            }

            res.add(board);
            return;
        }

        for (int col = 0; col < total; col++)
        {
            usedColumns[curRow] = col;

            if (isValidSolution(curRow, usedColumns))
            {
                dfs(res, usedColumns, curRow + 1, total);
            }

            usedColumns[curRow] = -1;
        }
    }

    private boolean isValidSolution(int curRow, int[] usedColumns)
    {
        for (int row = 0; row < curRow; row++)
        {
            if (usedColumns[row] == usedColumns[curRow]
                    || curRow - row == Math.abs(usedColumns[row] - usedColumns[curRow]))
            {
                return false;
            }
        }

        return true;
    }
}


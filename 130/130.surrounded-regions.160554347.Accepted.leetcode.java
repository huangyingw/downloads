public class Solution
{
    int[] unitArray;    //集合编号（隶属于哪一类）
    boolean[] edge; //是否被包围，每一类的edge都应该相同

    public void solve(char[][] board)
    {
        if (board.length < 3 || board[0].length < 3)
        {
            return;
        }

        unitArray = new int[board.length * board[0].length];
        edge = new boolean[unitArray.length];

        //initial the array
        for (int i = 0; i < unitArray.length; i++)
        {
            unitArray[i] = i;
        }

        for (int i = 0; i < unitArray.length; i++)
        {
            int r = i / board[0].length;
            int c = i % board[0].length;
            edge[i] = (board[r][c] == 'O' && (r == 0 || r == board.length - 1 || c == 0 || c == board[0].length - 1));  // true表示没有被包围
        }

        // span the matrix
        for (int i = 0; i < unitArray.length; i++)
        {
            int r = i / board[0].length;
            int c = i % board[0].length;
            int up = r - 1;
            int pre = c - 1;

            //the unper field
            if (up >= 0 && board[r][c] == board[up][c])
            {
                union_set(i, i - board[0].length);    //应该属于一类，union_set一下
            }

            //the pre field
            if (pre >= 0 && board[r][c] == board[r][pre])
            {
                union_set(i, i - 1);
            }
        }

        for (int i = 0; i < unitArray.length; i++)
        {
            int r = i / board[0].length;
            int c = i % board[0].length;

            if (board[r][c] == 'O' && !edge[find_set(i)])
            {
                board[r][c] = 'X';
            }
        }
    }

    private void union_set(int x, int y)
    {
        int rootX = find_set(x);   //找到这一类的根
        int rootY = find_set(y);
        boolean edgeU = this.edge[rootX] || this.edge[rootY];  //只要有一个被包围，则都被包围
        unitArray[rootX] = rootY;
        this.edge[rootY] = edgeU;
    }

    private int find_set(int x)
    {
        if (unitArray[x] == x)
        {
            return x;
        }

        unitArray[x] = find_set(unitArray[x]);
        return unitArray[x];
    }
}


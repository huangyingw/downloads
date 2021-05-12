public class Solution {
    public void wallsAndGates(int[][] rooms) {
        if (rooms == null || rooms.length == 0) {
            return;
        }
         
        int m = rooms.length;
        int n = rooms[0].length;
         
        boolean[][] visited = new boolean[m][n];
         
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (rooms[i][j] == 0) {
                    wallsAndGatesHelper(i, j, 0, visited, rooms);
                }
            }
        }
    }
     
    private void wallsAndGatesHelper(int row, int col, int distance, boolean[][] visited, int[][] rooms) {
        int rows = rooms.length;
        int cols = rooms[0].length;
         
        if (row < 0 || row >= rows || col < 0 || col >= cols) {
            return;
        }
         
        // visited
        if (visited[row][col]) {
            return;
        }
         
        // Is wall?
        if (rooms[row][col] == -1) {
            return;
        }
         
        // Distance greater than current
        if (distance > rooms[row][col]) {
            return;
        }
         
         
        // Mark as visited
        visited[row][col] = true;
         
        if (distance < rooms[row][col]) {
            rooms[row][col] = distance;
        }
         
        // go up, down, left and right
        wallsAndGatesHelper(row - 1, col, distance + 1, visited, rooms);
        wallsAndGatesHelper(row + 1, col, distance + 1, visited, rooms);
        wallsAndGatesHelper(row, col - 1, distance + 1, visited, rooms);
        wallsAndGatesHelper(row, col + 1, distance + 1, visited, rooms);
         
        // Mark as unvisited
        visited[row][col] = false;
    }
}

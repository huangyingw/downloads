public class Solution {
    public int shortestDistance(int[][] grid) {
        if (grid==null || grid.length==0 || grid[0].length==0) return -1;
        int m = grid.length;
        int n = grid[0].length;
        int[][] dist = new int[m][n];
        int[][] reach = new int[m][n];
        int houseNum = 0;
        int[][] directions = {{-1,0},{1,0},{0,-1},{0,1}};
        
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == 1) {
                    houseNum++;
                    int level = 0;
                    boolean[][] visited = new boolean[m][n];
                    LinkedList<Integer> queue = new LinkedList<Integer>();
                    queue.offer(i*n+j);
                    visited[i][j] = true;
                    while (!queue.isEmpty()) {
                        int size = queue.size();
                        for (int t=0; t<size; t++) {
                            int cur = queue.poll();
                            int x = cur/n;
                            int y = cur%n;
                            for (int[] dir : directions) {
                                int xnew = x + dir[0];
                                int ynew = y + dir[1];
                                if (xnew>=0 && xnew<m && ynew>=0 && ynew<n && !visited[xnew][ynew] && grid[xnew][ynew]==0) {
                                    queue.offer(xnew*n+ynew);
                                    visited[xnew][ynew] = true;
                                    dist[xnew][ynew] += level+1;
                                    reach[xnew][ynew]++;
                                }
                            }
                        }
                        level++;
                    }
                }
            }
        }
        
        int minDist = Integer.MAX_VALUE;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j]==0 && reach[i][j] == houseNum) {
                    minDist = Math.min(minDist, dist[i][j]);
                }
            }
        }
        return minDist==Integer.MAX_VALUE? -1 : minDist;
    }
}

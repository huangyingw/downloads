public class Solution {
    public int maxKilledEnemies(char[][] grid) {
        if(grid.length==0){ return 0; }
        int rowNo = grid.length, colNo = grid[0].length;
        int[] colHit = new int[colNo];
        int rowHit = 0;
        int result = 0;
       
        for(int i=0; i<rowNo; i++){
            for(int j=0; j<colNo; j++){
                if(j==0 || grid[i][j-1]=='W'){
                    rowHit = 0;
                    for(int k=j; k<colNo && grid[i][k] != 'W'; k++){
                        if(grid[i][k]=='E'){ rowHit++; }
                    }
                }
               
                if(i==0 || grid[i-1][j]=='W'){
                    colHit[j] = 0;
                    for(int k=i; k<rowNo && grid[k][j] != 'W'; k++){
                        if(grid[k][j]=='E'){ colHit[j]++; }
                    }
                }
               
                if(grid[i][j]=='0'){
                    result = Math.max(result, rowHit+colHit[j]);
                }
            }
        }
       
        return result;
    }
} 

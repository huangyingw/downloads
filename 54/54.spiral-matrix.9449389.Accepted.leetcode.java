  public class Solution {
    public ArrayList<Integer> spiralOrder(int[][] matrix) {
      int m = matrix.length, n = 0;

      if (m != 0) {
        n = matrix[0].length;
      }

      int cycle = m > n ? (n + 1) / 2 : (m + 1) / 2;
      ArrayList<Integer> res = new ArrayList<Integer>();
      int a = n, b = m;

      for (int i = 0; i < cycle; i++, a -= 2, b -= 2) {
        for (int column = i; column < i + a; column++) {
          res.add(matrix[i][column]);
        }

        for (int row = i + 1; row < i + b; row++) {
          res.add(matrix[row][i + a - 1]);
        }

        if (a == 1 || b == 1) {
          break;
        }

        for (int column = i + a - 2; column >= i; column--) {
          res.add(matrix[i + b - 1][column]);
        }

        for (int row = i + b - 2; row > i; row--) {
          res.add(matrix[row][i]);
        }
      }

      return res;
    }
  }


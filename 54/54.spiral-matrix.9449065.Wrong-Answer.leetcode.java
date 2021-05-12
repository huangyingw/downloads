  public class Solution {
    public ArrayList<Integer> spiralOrder(int[][] matrix) {
      int n = matrix.length;
      ArrayList<Integer> res = new ArrayList<Integer>();
      int k = 1;
      int top = 0, bottom = n - 1, left = 0, right = n - 1;

      while (left < right && top < bottom) {
        for (int j = left; j < right; j++) {
          res.add(k++);
        }

        for (int i = top; i < bottom; i++) {
          res.add(k++);
        }

        for (int j = right; j > left; j--) {
          res.add(k++);
        }

        for (int i = bottom; i > top; i--) {
          res.add(k++);
        }

        left++;
        right--;
        top++;
        bottom--;
      }

      if (n % 2 != 0) {
        res.add(k++);
      }

      return res;
    }
  }


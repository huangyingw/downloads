  public class Solution
  {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G,
                           int H)
    {
      int area = (C - A) * (D - B) + (G - E) * (H - F);

      if (C < E || G < A || D < F || H < B)
      {
        return area;
      }

      int[] X = { A, C, E, G };
      int[] Y = { B, D, F, H };
      return area - diff(X) * diff(Y);
    }

    private int diff(int[] X)
    {
      Arrays.sort(X);
      return X[2] - X[1];
    }
  }


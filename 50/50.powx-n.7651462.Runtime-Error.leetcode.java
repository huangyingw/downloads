	public class Solution {
		public double pow(double x, int n) {
			if (n < 0)
				return 1.0 / pow(x, -n);
			if (n == 0)
				return 1;
			double v = pow(x, n / 2);
			if (n % 2 == 0)
				return v * v;
			else
				return v * v * x;
		}
	}


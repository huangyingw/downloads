	public class Solution {
		public double power(double x, int n) {
			if (n == 0) {
				return 1;
			}

			double v = power(x, n / 2);
			return n % 2 == 0 ? v * v : v * v * x;
		}

		public double pow(double x, int n) {
			return n < 0 ? 1 / power(x, -n) : power(x, n);
		}
	}


public class Solution {
    private int mod = 1337;
    public int superPow(int a, int[] b) {
        int n = b.length;
		int ans = 1;
		for (int i = n - 1; i >= 0; i--) {
			ans = ans * quick_pow(a, b[i]) % mod;
			a = quick_pow(a, 10);
		}
		return ans;
	}
	
	int quick_pow(int a, int b) {
		int ans = 1;
		a %= mod;
		while (b > 0) {
			if ((b & 1) !=0) ans = ans * a % mod;
			a = a * a % mod;
			b >>= 1;
		}
		return ans;
	
    }
}

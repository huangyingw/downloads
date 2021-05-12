public class Solution {
    public int getMoneyAmount(int n) {
        int[][] dp = new int[n+1][n+1];
        return solve(dp, 1, n);
    }
    int solve(int[][] dp, int L, int R) {
		if (L >= R) return 0;
		if (dp[L][R] != 0) return dp[L][R];
		dp[L][R] = 0x7FFFFFFF;
		for (int i = L; i <= R; i++) {
			dp[L][R] = Math.min(dp[L][R], i + Math.max(solve(dp,L,i-1),solve(dp,i+1,R)));
		}
		return dp[L][R];
	}
}

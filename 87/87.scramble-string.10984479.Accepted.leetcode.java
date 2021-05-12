	public class Solution {
		public boolean isScramble(String s1, String s2) {
			if (s1.length() != s2.length()) {
				return false;
			}
            //动态规划解法
			int len = s1.length();
			boolean[][][] dp = new boolean[len + 1][len][len];

			for (int i = 0; i <= len - 1; i++)
				for (int j = 0; j <= len - 1; j++) {
					dp[1][i][j] = s1.charAt(i) == s2.charAt(j) ? true : false;
				}

			for (int k = 2; k <= len; k++)
				for (int i = 0; i <= len - k; i++)
					for (int j = 0; j <= len - k; j++) {
						dp[k][i][j] = false;

						for (int divlen = 1; divlen < k && !dp[k][i][j]; divlen++)
							dp[k][i][j] = (dp[divlen][i][j] && dp[k - divlen][i + divlen][j
									+ divlen])
									|| (dp[divlen][i][j + k - divlen] && dp[k - divlen][i
											+ divlen][j]);
					}

			return dp[len][0][0];
		}
	}



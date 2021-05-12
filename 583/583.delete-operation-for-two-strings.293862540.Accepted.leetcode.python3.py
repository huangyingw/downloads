class Solution:
    def minDistance(self, A, B):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if i == len(A) or j == len(B):
                    ans = len(A) + len(B) - i - j
                elif A[i] == B[j]:
                    ans = dp(i + 1, j + 1)
                else:
                    ans = 1 + min(dp(i + 1, j), dp(i, j + 1))
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)


class Solution(object):
    def longestPalindrome(self, s):
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        maxLength, result = 1, ""
        for index in range(len(s)):
            dp[index][index] = 1
            result = s[index]
        length = 2
        while length <= len(s):
            index_i = 0
            while index_i < len(s) - length + 1:
                index_j = index_i + length - 1
                if length == 2 and s[index_i] == s[index_j]:
                    dp[index_i][index_j] = 1
                    maxLength = max(maxLength, 2)
                    result = s[index_i:index_j + 1]
                elif s[index_i] == s[index_j] and dp[index_i + 1][index_j - 1]:
                    dp[index_i][index_j] = 1
                    if length > maxLength:
                        maxLength = length
                        result = s[index_i:index_j + 1]
                index_i += 1
            length += 1
        return result


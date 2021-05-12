class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        count = [256]
        i, numDistinct, maxLen = 0, 0, 0

        for j in range(0, len(s)):
            if count[s.charAt(j)] == 0:
                numDistinct += 1

            count[s.charAt(j)] += 1

            while numDistinct > 2:
                count[s.charAt(i)] -= 1

                if count[s.charAt(i)] == 0:
                    numDistinct -= 1
                i += 1
            maxLen = max(j - i + 1, maxLen)
        return maxLen


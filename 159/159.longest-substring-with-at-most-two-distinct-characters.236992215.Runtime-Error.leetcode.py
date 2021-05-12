class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        count = [0 for _ in range(256)]
        i, numDistinct, maxLen = 0, 0, 0

        for j in range(0, len(s)):
            if count[ord(s[j])] == 0:
                numDistinct += 1

            count[ord(s[j])] += 1

            while numDistinct > 2:
                count[ord(s[i])] -= 1

                i += 1
            maxLen = max(j - i + 1, maxLen)
        return maxLen


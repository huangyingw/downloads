class Solution:
    def maxPower(self, s: str) -> int:
        cur_max_length = max_length = 1

        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                cur_max_length += 1
            else:
                max_length = max(max_length, cur_max_length)
                cur_max_length = 1

        return max(max_length, cur_max_length)


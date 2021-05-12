class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        max_length = 0
        index = 0
        for i in range(len(s)):
            if s[i] in temp:
                max_length = max(max_length, i - index)
                while s[index] != s[i]:
                    temp.remove(s[index])
                    index += 1
                index += 1
            else:
                temp.add(s[i])
        return max(max_length, len(s) - index)


"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


class Solution:
    def numDecodings1(self, s):

        if not s or s == "0":
            return 0
        care, dont = 0, 1
        for i in range(1, len(s)):
            p, c = s[i - 1], s[i]
            if c == "0":
                if not (p == "1" or p == "2"):
                    return 0
                else:
                    care, dont = dont, 0
            elif p == "0":
                care, dont = 0, care
            else:
                if 11 <= int(p + c) <= 26:
                    care, dont = dont, dont + care
                else:
                    care, dont = 0, dont + care
        return dont + care

    def numDecodings2(self, s):
        v, w, p = 0, int(s > ''), ''
        for d in s:
            v, w, p = w, (d > '0') * w + (9 < int(p + d) < 27) * v, d
        return w


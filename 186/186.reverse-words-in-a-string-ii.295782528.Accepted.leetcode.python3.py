class Solution:
    def reverseWords(self, s):
        s.reverse()
        s.append(' ')
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                s[start:i] = reversed(s[start:i])
                start = i + 1
        s.pop()


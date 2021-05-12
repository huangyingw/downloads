class Solution:
    def reverseWords(self, s):
        self.reverse(s, 0, len(s) - 1)
        s.append(' ')
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse(s, start, i - 1)
                start = i + 1
        s.pop()

    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


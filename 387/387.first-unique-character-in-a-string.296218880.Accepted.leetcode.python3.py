class Solution:
    def firstUniqChar(self, s):
        if not s:
            return -1
        L = len(s)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            left = s.find(c)
            right = s.rfind(c)
            if 0 <= left < L and left == right:
                L = left
        return L if L < len(s) else -1


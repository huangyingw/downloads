class Solution(object):
    def read(self, buf, n):
        i = 0
        while i < n:
            buf4 = [''] * 4
            count = read4(buf4)
            count = min(count, n - i)
            i += count
        return i


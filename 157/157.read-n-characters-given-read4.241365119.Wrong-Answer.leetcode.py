class Solution(object):
    def read(self, buf, n):
        i = 0
        while i < n:
            buf4 = [''] * 4
            count = read4(buf4)
            if count == 0:
                break
            buf[i:] = buf4[:count]
            i += count
        return i


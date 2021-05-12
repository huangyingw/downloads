class Solution(object):
    def read(self, buf, n):
        pos, eof = 0, False
        while pos < n:
            buffer = [''] * 4
            sz = read4(buffer)
            if sz == 0:
                break
            buf[pos:] = buffer[:sz]
            pos += min(n - pos, sz)
        return pos


class Solution(object):
    def read(self, buf, n):
        pos, eof = 0, False
        buffer = [''] * 4
        while not eof and pos < n:
            sz = read4(buffer)
            for i in range(sz):
                buf[pos + i] = buffer[i]
            pos += min(n - pos, sz)
        return pos


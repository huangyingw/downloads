class Solution(object):
    def read(self, buf, n):
        pos, eof = 0, False
        while not eof and pos < n:
            buffer = [''] * 4
            sz = read4(buffer)
            if sz < 4:
                eof = True
            buf[pos:] = buffer[:sz]
            pos += min(n - pos, sz)
        return pos


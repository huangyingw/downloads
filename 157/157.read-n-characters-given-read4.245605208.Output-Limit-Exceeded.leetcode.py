class Solution(object):
    def read(self, buf, n):
        pos, eof = 0, False
        buffer = [''] * 4
        while not eof and pos < n:
            sz = read4(buffer)
            print('sz --> %s' % (sz))
            for i in range(sz):
                buf[pos + i] = buffer[i]
            pos += min(n - pos, sz)
            print('pos --> %s' % (pos))
        return pos


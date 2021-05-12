class Solution(object):
    def read(self, buf, n):
        count = 0
        while count < n:
            buffer = [''] * 4
            sz = read4(buffer)
            if sz == 0:
                break
            buf[count:] = buffer[:sz]
            count += min(n - count, sz)
        return count


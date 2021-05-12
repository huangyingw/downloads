class Solution(object):
    def read(self, buf, n):
        count, myBuffer, sz = 0, [None] * 4, 4
        while sz == 4 and count < n:
            sz = read4(myBuffer)
            buf[count:] = myBuffer[:sz]
            count += min(n - count, sz)
        return count


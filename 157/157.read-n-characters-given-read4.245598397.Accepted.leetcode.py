class Solution(object):
    def read(self, buf, n):
        count = 0
        myBuffer = [None] * 4
        while count < n:
            sz = read4(myBuffer)
            if sz == 0:
                break
            buf[count:] = myBuffer[:sz]
            count += min(n - count, sz)
        return count


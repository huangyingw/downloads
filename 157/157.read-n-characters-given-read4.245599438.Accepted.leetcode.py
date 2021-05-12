class Solution(object):
    def read(self, buf, n):
        idx = 0
        myBuffer = [None] * 4
        while idx < n:
            myBuffer = [''] * 4
            count = read4(myBuffer)
            if count == 0:
                break
            count = min(count, n - idx)
            buf[idx:] = myBuffer[:count]
            idx += count
        return idx


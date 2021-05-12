class Solution(object):
    def read(self, buf, n):
        count = 0
        myBuffer = [None] * 4
        while count < n:
            sz = read4(myBuffer)
            if sz == 0:
                break
            index = 0
            while index < sz and count < n:
                buf[count] = myBuffer[index]
                count += 1
                index += 1
        return count


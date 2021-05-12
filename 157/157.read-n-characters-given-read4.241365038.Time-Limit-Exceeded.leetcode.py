class Solution(object):
    def read(self, buf, n):
        count = 0
        myBuffer = [None] * 4
        while count < n:
            num = read4(myBuffer)
            index = 0
            while index < num and count < n:
                buf[count] = myBuffer[index]
                count += 1
                index += 1
        return count


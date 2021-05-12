class Solution(object):
    def __init__(self):
        self.buffer = [None for _ in range(4)]
        self.oneRead = 0
        self.offset = 0

    def read(self, buf, n):
        lessthan4 = False
        haveRead = 0

        while not lessthan4 and haveRead < n:
            if self.oneRead == 0:
                self.oneRead = read4(self.buffer)
                lessthan4 = self.oneRead < 4

            actRead = min(n - haveRead, self.oneRead)

            for i in range(0, actRead):
                print("i --> %s" % (i))
                buf[haveRead + i] = self.buffer[self.offset + i]

            self.oneRead -= actRead
            self.offset = (self.offset + actRead) % 4
            print("self.offset --> %s" % (self.offset))
            haveRead += actRead
        return haveRead


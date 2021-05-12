class Solution(object):
    buffer = [None for _ in range(4)]
    oneRead = 0
    offset = 0

    def read(self, buf, n):
        lessthan4 = False
        haveRead = 0

        while not lessthan4 and haveRead < n:
            if Solution.oneRead == 0:
                Solution.oneRead = read4(Solution.buffer)
                lessthan4 = Solution.oneRead < 4

            actRead = min(n - haveRead, Solution.oneRead)

            for i in range(0, actRead):
                print("Solution.offset --> %s" % (Solution.offset))
                print("Solution.offset + i --> %s" % (Solution.offset + i))
                buf[haveRead + i] = Solution.buffer[Solution.offset + i]

            Solution.oneRead -= actRead
            Solution.offset = (Solution.offset + actRead) % 4
            haveRead += actRead
        return haveRead


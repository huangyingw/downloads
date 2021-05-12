from collections import deque


class Solution(object):
    def numSquares(self, n):
        if n < 0:
            return -1
        # corner case 2
        if n == 0:
            return 1
        q = deque()
        visited = set()
        # val, step
        q.append((0, 0))
        visited.add(0)

        while q:
            val, step = q.popleft()
            for i in xrange(1, n + 1):
                tmp = val + i**2
                if tmp > n:
                    break
                if tmp == n:
                    return step + 1
                else:
                    if tmp not in visited:
                        visited.add(tmp)
                        q.append((tmp, step + 1))

        # Should never reach here
        return -1


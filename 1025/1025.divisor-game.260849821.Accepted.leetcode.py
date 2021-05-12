class Solution(object):
    def divisorGame(self, N):
        if N == 0:
            return False
        move = 0
        while N > 1:
            for num in range(1, N):
                if N % num == 0:
                    N -= num
                    move += 1
                    break
        if move % 2:
            return True
        return False


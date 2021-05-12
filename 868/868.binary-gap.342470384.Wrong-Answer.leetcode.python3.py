class Solution(object):
    def binaryGap(self, N):
        previous, max_gap = None, 0
        i = 0
        while N > 0:
            if N & 1:
                if previous:
                    max_gap = max(max_gap, i - previous)
                previous = i
            N >>= 1
            i += 1
        return max_gap


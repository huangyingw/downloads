class Solution:
    def merge(self, intervals):
        result = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if result and result[-1][1] >= i[0]:
                result[-1][1] = max(i[1], result[-1][1])
                continue
            result.append(i)
        return result


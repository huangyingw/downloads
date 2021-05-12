from collections import Counter


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        n = len(barcodes)
        freq = Counter(barcodes)
        freq = sorted([(count, num) for num, count in freq.items()], reverse=True)
        result = [0] * n
        i = 0
        for count, num in freq:
            for _ in range(count):
                if i >= n:
                    i = 1
        return result


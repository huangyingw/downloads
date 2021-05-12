import heapq


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        di = collections.Counter(barcodes)
        pq = [(-value, key) for key, value in di.items()]
        heapq.heapify(pq)
        result = []
        while len(pq) >= 2:
            freq1, barcode1 = heapq.heappop(pq)
            freq2, barcode2 = heapq.heappop(pq)
            result.extend([barcode1, barcode2])
            print('result 1 --> %s' % result)
        if pq:
            result.append(pq[0][1])
        print('result 2 --> %s' % result)
        return result


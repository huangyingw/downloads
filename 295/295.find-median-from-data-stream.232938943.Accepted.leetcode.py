from heapq import *


class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        heappush(self.maxHeap, -num)
        minTop = self.minHeap[0] if len(self.minHeap) else None
        maxTop = self.maxHeap[0] if len(self.maxHeap) else None
        if minTop < -maxTop or len(self.minHeap) + 1 < len(self.maxHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self):
        if len(self.minHeap) < len(self.maxHeap):
            return -1.0 * self.maxHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0


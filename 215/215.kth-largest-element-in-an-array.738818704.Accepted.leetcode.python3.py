class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []
        import heapq
        for num in nums:
            heapq.heappush(heap, -(num))
        result = 0
        for _ in range(k):
            result = heapq.heappop(heap)
        return -(result)


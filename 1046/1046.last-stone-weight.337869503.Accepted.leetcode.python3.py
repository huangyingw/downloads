import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))
        return -stones[0]


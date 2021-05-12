class Solution(object):
    def kthSmallest(self, matrix, k):
        if not matrix:
            return 0
        heap = []
        for col in range(len(matrix[0])):
            heapq.heappush(heap, (matrix[0][col], 0, col))
        val = 0
        for index in range(k):
            val, row, col = heapq.heappop(heap)
            new_val = float('inf')
            if row < len(matrix) - 1:
                new_val = matrix[row + 1][col]
            heapq.heappush(heap, (new_val, row + 1, col))
        return val


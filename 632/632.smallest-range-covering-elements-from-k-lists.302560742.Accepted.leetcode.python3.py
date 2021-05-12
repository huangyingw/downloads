import heapq


class Solution:
    def smallestRange(self, nums):
        queue = [(list_num[0], i, 0) for i, list_num in enumerate(nums)]
        heapq.heapify(queue)
        result = [float("-inf"), float("inf")]
        right = max(row[0] for row in nums)
        while queue:
            left, i, j = heapq.heappop(queue)
            if right - left < result[1] - result[0]:
                result = [left, right]
            if j == len(nums[i]) - 1:
                return result
            next_num_val = nums[i][j + 1]
            right = max(right, next_num_val)
            heapq.heappush(queue, (next_num_val, i, j + 1))


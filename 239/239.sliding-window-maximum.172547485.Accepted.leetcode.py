class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []

        dequeue = []
        result = [0 for _ in range(len(nums) - k + 1)]

        for idx in range(len(nums)):
            while dequeue and nums[dequeue[-1]] < nums[idx]:
                dequeue.pop(-1)

            dequeue.append(idx)

            if idx + 1 < k:
                continue

            while dequeue[-1] - dequeue[0] + 1 > k:
                dequeue.pop(0)

            result[idx + 1 - k] = nums[dequeue[0]]

        return result


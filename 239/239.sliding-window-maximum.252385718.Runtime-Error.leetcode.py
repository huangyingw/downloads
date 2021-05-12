from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        result = []
        q = deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        for i in range(k, len(nums)):
            result.append(nums[q[0]])
            while q and q[0] <= i - k:
                q.popleft()
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        result.append(nums[q[0]])
        return result


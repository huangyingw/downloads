from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q = deque()
        max_window = []
        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            if q[0] <= i - k:
                q.popleft()
            if i >= k - 1:
                max_window.append(nums[q[0]])
        return max_window


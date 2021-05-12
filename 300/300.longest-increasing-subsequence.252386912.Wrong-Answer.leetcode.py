class Solution(object):
    def lengthOfLIS(self, nums):
        dequeue = []
        result = []
        for idx in range(len(nums)):
            while dequeue and nums[dequeue[-1]] > nums[idx]:
                dequeue.pop()
            dequeue += [idx]
            result = min(result, len(dequeue))
        return result


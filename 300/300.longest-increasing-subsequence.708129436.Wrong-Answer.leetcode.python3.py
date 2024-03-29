class Solution(object):
    def lengthOfLIS(self, nums):
        dequeue = []
        result = 0
        for idx in range(len(nums)):
            while dequeue and nums[dequeue[-1]] >= nums[idx]:
                dequeue.pop()
            dequeue += [idx]
            print("dequeue --> %s" % dequeue)
            result = max(result, len(dequeue))
        return result


class Solution(object):
    def maximumGap(self, nums):
        if not nums or nums.length < 2:
            return 0

        min = nums[0]
        max = nums[0]

        for i in nums:

            min = min(min, i)
            max = max(max, i)

        gap = ceil((float)(max - min) / (len(nums) - 1))
        bucketsMIN = [sys.maxint for _ in range(len(nums) - 1)]
        bucketsMAX = [-sys.maxint - 1 for _ in range(len(nums) - 1)]

        for i in nums:
            if i == min or i == max:
                continue

            idx = (i - min) / gap
            bucketsMIN[idx] = min(i, bucketsMIN[idx])
            bucketsMAX[idx] = max(i, bucketsMAX[idx])

        maxGap = -sys.maxint - 1
        previous = min

        for i in range(0, len(nums) - 1):
            if bucketsMIN[i] == sys.maxint and bucketsMAX[i] == -sys.maxint - 1:
                continue

            maxGap = max(maxGap, bucketsMIN[i] - previous)
            previous = bucketsMAX[i]

        maxGap = max(maxGap, max - previous)
        return maxGap


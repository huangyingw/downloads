class Solution(object):
    def maximumGap(self, nums):
        if not nums or len(nums) < 2:
            return 0

        vmin = nums[0]
        vmax = nums[0]

        for i in nums:
            vmin = min(vmin, i)
            vmax = max(vmax, i)

        gap = math.ceil((float)(vmax - vmin) / (len(nums) - 1))
        bucketsMIN = [sys.maxint for _ in range(len(nums) - 1)]
        bucketsMAX = [-sys.maxint - 1 for _ in range(len(nums) - 1)]

        for i in nums:
            if i == vmin or i == vmax:
                continue

            idx = (i - vmin) / gap
            bucketsMIN[idx] = min(i, bucketsMIN[idx])
            bucketsMAX[idx] = max(i, bucketsMAX[idx])

        maxGap = -sys.maxint - 1
        previous = vmin

        for i in range(0, len(nums) - 1):
            if bucketsMIN[i] == sys.maxint and bucketsMAX[i] == -sys.maxint - 1:
                continue

            maxGap = max(maxGap, bucketsMIN[i] - previous)
            previous = bucketsMAX[i]

        maxGap = max(maxGap, vmax - previous)
        return maxGap


class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        lower = min(nums)
        difference = max(nums) - lower
        gaps = len(nums) - 1
        if difference == 0:
            return 0
        width = difference // gaps
        if width == 0:
            width = 1
        nb_buckets = 1 + difference // width
        buckets = [[None, None] for _ in range(nb_buckets)]
        for num in nums:
            bucket = (num - lower) // width
            buckets[bucket][0] = min(buckets[bucket][0], num) if buckets[bucket][0] != None else num
            buckets[bucket][1] = max(buckets[bucket][1], num) if buckets[bucket][1] != None else num
        last_used_bucket = 0
        max_gap = difference // gaps
        for i in range(nb_buckets - 1):
            if not buckets[i][0] and buckets[i + 1][0]:
                max_gap = max(max_gap, buckets[i + 1][0] - buckets[last_used_bucket][1])
            elif buckets[i][0]:
                last_used_bucket = i
        return max_gap


class Solution(object):
    def smallestDistancePair(self, nums, k):
        def k_pair_distances(diff):
            count, j = 0, 0
            for i, num in enumerate(nums):
                while num - nums[j] > diff:
                    j += 1
                count += i - j
            return count >= k
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if k_pair_distances(mid):
                right = mid
            else:
                left = mid + 1
        return left


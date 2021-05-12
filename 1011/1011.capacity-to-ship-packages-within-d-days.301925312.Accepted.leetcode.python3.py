class Solution(object):
    def shipWithinDays(self, weights, D):
        left, right = max(weights), sum(weights)
        while left < right:
            curr_sum, groups, invalid = 0, 0, True
            mid = left + ((right - left) >> 1)
            for weight in weights:
                if weight > mid:
                    invalid = False
                    break
                if curr_sum + weight > mid:
                    groups += 1
                    curr_sum = 0
                curr_sum += weight
            if invalid and groups < D:
                right = mid
            else:
                left = mid + 1
        return left


class Solution(object):
    ELEMENTS = 4

    def fourSum(self, nums, target):
        results = []
        self.n_sum(sorted(nums), target, [], self.ELEMENTS, results)
        return results

    def n_sum(self, nums, target, partial, n, results):
        if len(nums) < n or target > nums[-1] * n or target < nums[0] * n:
            return
        if n == 2:
            left = 0
            right = len(nums) - 1
            while left < right:
                if left - 1 > 0 and nums[left] == nums[left - 1]:
                    left += 1
                elif right + 1 <= len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                elif nums[left] + nums[right] == target:
                    results.append(partial + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(len(nums) - n + 1):
                if i - 1 > 0 and nums[i] == nums[i - 1]:
                    continue
                self.n_sum(nums[i + 1:], target - nums[i], partial + [nums[i]], n - 1, results)


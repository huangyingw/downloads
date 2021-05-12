class Solution(object):
    def threeSumClosest(self, nums, target):
        min = sys.maxint
        result = 0
        nums.sort()

        for i in range(0, len(nums)):
            j = i + 1
            k = nums.length - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                diff = abs(sum - target)

                if diff < min:
                    min = diff
                    result = sum
                if sum <= target:
                    j += 1
                else:
                    k -= 1
        return result


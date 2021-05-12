class Solution(object):
    def threeSum(self, nums):
        result = []

        if len(nums) < 3:
            return result

        nums.sort()

        for i in range(0, len(nums) - 2):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                if k + 1 < len(nums) and nums[k] == nums[k + 1]:
                    k -= 1
                    continue

                if j - 1 > i and nums[j] == nums[j - 1]:
                    j += 1
                    continue

                if nums[i] + nums[j] + nums[k] == 0:
                    temp = []
                    temp.add(nums[i])
                    temp.add(nums[j])
                    temp.add(nums[k])
                    result.add(temp)
                    k -= 1
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1

        return result


class Solution(object):
    def threeSum(self, nums):
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        for i in range(len(nums) - 2):
            print("nums[i] nums[%s] --> %s" % (i, nums[i]))
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                if j - 1 >= i + 1 and nums[j] == nums[j - 1]:
                    print("nums[j] nums[%s] --> %s" % (j, nums[j]))
                    j += 1
                    continue
                if k + 1 <= len(nums) - 1 and nums[k] == nums[k + 1]:
                    print("nums[k] nums[%s] --> %s" % (k, nums[k]))
                    k -= 1
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result += [[nums[i], nums[j], nums[k]]]
                    print("result --> %s" % result)
                    k -= 1
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    print("nums[k] > 0: nums[%s] --> %s" % (k, nums[k]))
                    k -= 1
                else:
                    print("nums[j] < 0: nums[%s] --> %s" % (j, nums[j]))
                    j += 1
        return result


class Solution(object):
    def fourSum(self, nums, target):
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, len(nums) - 1
                while k < l:
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        k += 1
                        continue
                    ss = nums[i] + nums[j] + nums[k] + nums[l]
                    if ss < target:
                        k += 1
                    elif ss > target:
                        l -= 1
                    elif ss == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
        return result


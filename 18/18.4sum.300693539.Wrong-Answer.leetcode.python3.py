class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        ret = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    ss = nums[i] + nums[j] + nums[left] + nums[right]
                    if ss == target:
                        ret.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif ss < target:
                        left += 1
                    else:
                        right -= 1
        return ret


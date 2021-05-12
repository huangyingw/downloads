class Solution(object):
    def findNumberOfLIS(self, nums):
        length = [1] * len(nums)
        count = [1] * len(nums)
        result = 0
        for end, num in enumerate(nums):
            for start in range(end):
                if num > nums[start]:
                    if length[start] >= length[end]:
                        length[end] = 1 + length[start]
                        count[end] = count[start]
                    elif length[start] + 1 == length[end]:
                        count[end] += count[start]
        for index, max_subs in enumerate(count):
            if length[index] == max(length):
                result += max_subs
        return result


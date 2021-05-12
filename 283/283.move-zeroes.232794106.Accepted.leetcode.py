class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        tags = []
        for num in nums:
            count += 1
            if num == 0:
                if str(count - 1) not in tags:
                    tags.append(count - 1)
        for tag in tags[::-1]:
            del nums[tag]
            nums.append(0)


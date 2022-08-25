class Solution(object):
    def findKthLargest(self, nums, k):
        random.shuffle(nums)
        return self.quickSelection(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSelection(self, nums, start, end, k):
        if start > end:
            return float('inf')
        pivot = nums[end]
        left = start
        for i in range(start, end):
            if nums[i] <= pivot:

                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        nums[left], nums[end] = nums[end], nums[left]
        if left == k:
            return nums[left]
        elif left < k:
            return self.quickSelection(nums, left + 1, end, k)
        else:
            return self.quickSelection(nums, start, left - 1, k)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        print('start --> %s' % nums[start])
        print('end --> %s' % nums[end])
        if nums[end] < target:
            return end + 1
        if nums[start] > target:
            return max(start - 1, 0)
        return min(start + 1, len(nums) - 1)


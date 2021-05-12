class Solution(object):
    def findKthLargest(self, nums, k):
        def partition(start, end):
            pivot = nums[start]
            left = start + 1
            right = end

            nums[start] = nums[right]
            nums[right] = pivot
            return right

        def select(left, right):
            pivot = partition(left, right)

            if pivot + 1 == k:
                return nums[pivot]
            elif pivot + 1 > k:
                return select(left, pivot - 1)
            else:
                return select(pivot + 1, right)

        return select(0, len(nums) - 1)


class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.convert(nums, 0, len(nums) - 1)

    def convert(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.convert(nums, left, mid - 1)
        root.right = self.convert(nums, mid + 1, right)
        return root


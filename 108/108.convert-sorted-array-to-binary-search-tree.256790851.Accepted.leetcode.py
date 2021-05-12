class Solution(object):
    def sortedArrayToBST(self, nums):
        def sortedArrayToBST(nums, left, right):
            if left > right:
                return None
            mid = (left + right) / 2
            root = TreeNode(nums[mid])
            root.left = sortedArrayToBST(nums, left, mid - 1)
            root.right = sortedArrayToBST(nums, mid + 1, right)
            return root
        return sortedArrayToBST(nums, 0, len(nums) - 1)


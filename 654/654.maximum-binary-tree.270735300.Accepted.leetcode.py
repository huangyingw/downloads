class Solution():
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        l, r = 0, len(nums) - 1
        root = nums.index(max(nums))
        node = TreeNode(nums[root])
        node.left = self.constructMaximumBinaryTree(nums[:root])
        node.right = self.constructMaximumBinaryTree(nums[root + 1:])
        return node


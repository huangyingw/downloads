class Solution(object):
    def sortedListToBST(self, head):
        def sortedArrayToBST(nums, left, right):
            if left > right:
                return None

            mid = (left + right) / 2
            root = TreeNode(nums[mid])
            root.left = sortedArrayToBST(nums, left, mid - 1)
            root.right = sortedArrayToBST(nums, mid + 1, right)
            return root
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        return sortedArrayToBST(nums, 0, len(nums) - 1)


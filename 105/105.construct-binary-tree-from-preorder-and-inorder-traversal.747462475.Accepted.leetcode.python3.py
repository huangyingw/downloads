class Solution:
    def buildTree(self, preorder, inorder):
        inorderDict = {num: i for i, num in enumerate(inorder)}
        pre = iter(preorder)

        def helper(start, end):
            if start > end:
                return None
            val = next(pre)
            root = TreeNode(val)
            idx = inorderDict[val]
            root.left = helper(start, idx - 1)
            root.right = helper(idx + 1, end)
            return root
        return helper(0, len(inorder) - 1)


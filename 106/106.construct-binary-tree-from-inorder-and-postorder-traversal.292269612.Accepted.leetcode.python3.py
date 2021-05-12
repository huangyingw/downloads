class Solution:
    def buildTree(self, inorder, postorder):
        inorderDict = {num: i for i, num in enumerate(inorder)}

        def helper(start, end):
            if start > end:
                return None
            rootVal = postorder.pop()
            root = TreeNode(rootVal)
            idx = inorderDict[rootVal]
            root.right = helper(idx + 1, end)
            root.left = helper(start, idx - 1)
            return root
        return helper(0, len(inorder) - 1)


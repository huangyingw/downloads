class Solution(object):
    def buildTree(self, preorder, inorder):
        map = {}
        for idx, val in enumerate(inorder):
            map[val] = idx

        def dfs(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight:
                return None

            root = TreeNode(preorder[preLeft])
            idx = map[preorder[preLeft]]
            root.right = dfs(preRight - inRight + idx +
                             1, preRight, idx + 1, inRight)
            root.left = dfs(preLeft + 1, preLeft +
                            idx - inLeft, inLeft, idx - 1)
            return root

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)


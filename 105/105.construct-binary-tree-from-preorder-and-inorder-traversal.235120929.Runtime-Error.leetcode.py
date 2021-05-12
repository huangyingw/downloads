class Solution(object):
    def buildTree(self, preorder, inorder):
        map = {}
        for idx, val in enumerate(inorder):
            map[val] = idx
        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)

        def dfs(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight:
                return None

            root = TreeNode(preorder[preLeft])
            idx = map[preorder[preLeft]]
            root.left = dfs(preLeft + 1, preLeft + idx - inLeft, inLeft, idx - 1)
            root.right = dfs(preRight - inRight + idx + 1, preRight, idx + 1, inRight)
            return root


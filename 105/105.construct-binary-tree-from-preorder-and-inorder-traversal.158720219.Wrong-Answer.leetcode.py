class Solution(object):
    def buildTree(self, preorder, inorder):
        map = {}
        for idx, val in enumerate(inorder):
            map[val] = idx

        def dfs(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight:
                return None

            root = TreeNode(preorder[preLeft])
            map[preorder[preLeft]]
            return root

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)


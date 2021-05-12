class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        map = {}
        for idx, val in enumerate(inorder):
            map[val] = idx

        def helper(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight:
                return None

            root = TreeNode(preorder[preLeft])
            idx = map[preorder[preLeft]]
            root.left = helper(preLeft + 1, preLeft +
                               idx - inLeft, inLeft, idx - 1)
            root.right = helper(preRight - inRight + idx +
                                1, preRight, idx + 1, inRight)
            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


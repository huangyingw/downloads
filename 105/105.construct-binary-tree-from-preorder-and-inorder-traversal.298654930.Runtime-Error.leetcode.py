class Solution(object):
    def buildTree(self, preorder, inorder):
        self.index = 0

        def recursive(preorder, inorder, start, end):
            if start > end:
                return None
            node = TreeNode(preorder[self.index])
            self.index += 1
            if start == end:
                return node
            search_index = 0
            for i in range(start, end + 1):
                if inorder[i] == node.val:
                    search_index = i
                    break
            node.right = recursive(preorder, inorder, search_index + 1, end)
            node.left = recursive(preorder, inorder, start, search_index - 1)
            return node
        return recursive(preorder, inorder, 0, len(inorder) - 1)


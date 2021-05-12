class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        inorder_index = inorder.index(postorder.pop())
        root = TreeNode(inorder[inorder_index])
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        root.right = self.buildTree(inorder[inorder_index + 1:], postorder)
        return root


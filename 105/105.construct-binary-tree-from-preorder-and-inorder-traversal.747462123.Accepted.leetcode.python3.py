class Solution(object):
    def buildTree(self, preorder, inorder):
        def build(stop):
            if not inorder or inorder[-1] == stop:
                return None
            root_val = preorder.pop()
            root = TreeNode(root_val)
            root.left = build(root_val)
            inorder.pop()
            root.right = build(stop)
            return root
        preorder.reverse()
        inorder.reverse()
        return build(None)


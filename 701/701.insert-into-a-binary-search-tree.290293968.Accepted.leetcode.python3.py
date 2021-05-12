class Solution(object):
    def insertIntoBST(self, root, val):
        node = TreeNode(val)
        cur = root
        if not root:
            return node
        while root:
            if root.val <= val:
                if not root.right:
                    root.right = node
                    return cur
                root = root.right
            else:
                if not root.left:
                    root.left = node
                    return cur
                root = root.left


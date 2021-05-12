class Solution(object):
    def inorderSuccessor(self, root, p):
        ans = None
        while root:
            if p.val < root.val:
                ans = root
                root = root.left
            else:
                root = root.right
        return ans


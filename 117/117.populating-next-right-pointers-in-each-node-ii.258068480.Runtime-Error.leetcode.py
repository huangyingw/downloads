class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        if not root.left and not root.right:
            return
        root.left.next = root.right
        if root.next and root.right:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)


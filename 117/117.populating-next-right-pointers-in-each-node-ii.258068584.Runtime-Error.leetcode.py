class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        dummy = TreeLinkNode(-1)
        node = dummy
        while root:
            while root:
                node.next = root.left
                node = node.next or node
                node.next = root.right
                node = node.next or node
                root = root.next
            root, node = dummy.next, dummy


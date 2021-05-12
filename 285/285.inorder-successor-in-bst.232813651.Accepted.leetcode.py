class Solution(object):
    def inorderSuccessor(self, root, p):
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            l.append(root)
            inOrder(root.right)

        l = []
        inOrder(root)
        for i in range(len(l)):
            if l[i] == p:
                return l[i + 1] if i + 1 < len(l) else None


class Solution:
    def connect(self, root):
        nav = None
        while root:
            if root.left:
                if nav:
                    nav.next = root.left
                nav = root.left
            if root.right:
                if nav:
                    nav.next = root.right
                nav = root.right
            root = root.next


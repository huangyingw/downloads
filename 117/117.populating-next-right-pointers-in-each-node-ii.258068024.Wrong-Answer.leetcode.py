class Solution:
    def connect(self, root):
        if root:
            if root.left and root.right:
                root.left.next = root.right
                tmp = root.next
                while tmp:
                    if tmp.left:
                        root.right.next = tmp.left
                        break
                    if tmp.right:
                        root.right.next = tmp.right
                        break
                    tmp = tmp.next
            elif root.left:
                tmp = root.next
                while tmp:
                    if tmp.left:
                        root.left.next = tmp.left
                        break
                    if tmp.right:
                        root.left.next = tmp.right
                        break
                    tmp = tmp.next
            elif root.right:
                tmp = root.next
                while tmp:
                    if tmp.left:
                        root.right.next = tmp.left
                        break
                    if tmp.right:
                        root.right.next = tmp.right
                        break
                    tmp = tmp.next
            self.connect(root.right)
            self.connect(root.left)


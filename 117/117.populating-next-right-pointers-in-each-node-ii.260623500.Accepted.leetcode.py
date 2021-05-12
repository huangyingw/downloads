class Solution:
    def connect(self, root):
        if not root:
            return

        level, prev = [root], root
        while level:
            new_level, prev.Next, prev = [], None, None
            for node in level:
                if node.left:
                    if prev:
                        prev.next = node.left
                    prev = node.left
                    new_level.append(node.left)
                if node.right:
                    if prev:
                        prev.next = node.right
                    prev = node.right
                    new_level.append(node.right)
            level = new_level
        return root


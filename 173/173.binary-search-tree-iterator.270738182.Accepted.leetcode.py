class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return True if self.stack else False

    def next(self):
        node = self.stack.pop()
        result = node.val
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return result


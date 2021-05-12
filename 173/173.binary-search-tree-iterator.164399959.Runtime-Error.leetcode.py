class BSTIterator(object):
    def __init__(self, root):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return self.stack != []

    def next(self):
        root = self.stack.pop()
        result = root.val
        root = root.right

        while root:
            self.stack.push(root)
            root = root.left
        return result


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.fill_stack(root)

    def next(self) -> int:

        node = self.stack.pop()
        self.fill_stack(node.right)
        return node.val

    def hasNext(self) -> bool:

        return len(self.stack) > 0

    def fill_stack(self, root):
        while root:
            self.stack.append(root)
            root = root.left


class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
            while node:
                stack.append(node)
                node = node.left


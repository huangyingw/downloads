class Solution(object):
    def convertBST(self, root):
        total = 0
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
        return root


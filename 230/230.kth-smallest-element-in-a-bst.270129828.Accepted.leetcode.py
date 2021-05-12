class Solution(object):
    def kthSmallest(self, root, k):
        result = []
        stack = [root]
        while stack:
            if root:
                stack += [root]
                root = root.left
            else:
                root = stack.pop()
                k -= 1
                if k == 0:
                    return root.val
                root = root.right
        return result


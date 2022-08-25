class Solution(object):
    def kthSmallest(self, root, k):

        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


class Solution1:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        cur = root

        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                k -= 1
                if not k:
                    return node.val
                cur = node.right


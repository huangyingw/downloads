class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []

        def helper(root, level):
            if not root:
                return

            if level >= len(res):
                res.append(root.val)
            helper(root.right, level + 1)
            helper(root.left, level + 1)

        helper(root, 0)
        return res


class Solution1:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return

        res, queue = [], [root]

        while queue:
            new_level = []
            temp_val = None

            for node in queue:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)

            res.append(queue[-1].val)
            queue = new_level if new_level else None

        return res


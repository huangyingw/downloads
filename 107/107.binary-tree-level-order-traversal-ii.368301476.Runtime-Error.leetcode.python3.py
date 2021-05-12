class Solution_Iterative:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        current, res = [root], []

        while current:
            nex, temp = [], []
            for n in current:
                temp.append(n.val)
                if n.left:
                    nex.append(n.left)
                if n.right:
                    nex.append(n.right)
            current = nex
            res.append(temp)
        return res[::-1]


class Solution_Recursive:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        def helper(node, level):

            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)

        return levels[::-1]


class Solution(object):
    def rightSideView(self, root):

        def dfs(root, level):
            if not root:
                return

            self.level_to_node[level] = root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        self.level_to_node = {}
        dfs(root, 0)
        return self.level_to_node.values()


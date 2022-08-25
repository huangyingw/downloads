class Solution(object):
    def zigzagLevelOrder(self, root):
        def dfs(root, level, result=[], leftToRight=True):
            if leftToRight:
                result[level].append(root.val)
            else:
                result[level].insert(0, root.val)
            dfs(root.left, level + 1, result, not leftToRight)
            dfs(root.right, level + 1, result, not leftToRight)
        result = []
        dfs(root.left, 0, result, True)
        dfs(root.right, 0, result, True)
        return result


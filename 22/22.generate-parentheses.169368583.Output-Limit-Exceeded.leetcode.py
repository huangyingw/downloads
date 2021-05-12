class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def dfs(current, left, right):
            print('current --> %s' % current)
            print('left --> %s' % left)
            print('right --> %s' % right)
            if right > left:
                return

            if right == n:
                result.append(current)

            dfs(current + '(', left + 1, right)
            dfs(current + ')', left, right + 1)

        dfs('', 0, 0)
        return result


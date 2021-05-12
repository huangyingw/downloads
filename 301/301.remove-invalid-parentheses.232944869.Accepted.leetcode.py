class Solution(object):
    def removeInvalidParentheses(self, s):
        if not s:
            return ['']
        left_remove = right_remove = 0
        for c in s:
            if c == '(':
                left_remove += 1
            elif c == ')':
                if left_remove:
                    left_remove -= 1
                else:
                    right_remove += 1

        ans = set()
        self.dfs(0, left_remove, right_remove, 0, '', s, ans)
        return list(ans)

    def dfs(self, index, left_remove, right_remove, left_pare, cur, s, ans):
        if left_remove < 0 or right_remove < 0 or left_pare < 0:
            return
        if index == len(s):
            if left_remove == right_remove == left_pare == 0:
                ans.add(cur)
            return

        if s[index] == '(':
            self.dfs(index + 1, left_remove - 1, right_remove, left_pare, cur, s, ans)
            self.dfs(index + 1, left_remove, right_remove, left_pare + 1, cur + s[index], s, ans)
        elif s[index] == ')':
            self.dfs(index + 1, left_remove, right_remove - 1, left_pare, cur, s, ans)
            self.dfs(index + 1, left_remove, right_remove, left_pare - 1, cur + s[index], s, ans)
        else:
            self.dfs(index + 1, left_remove, right_remove, left_pare, cur + s[index], s, ans)


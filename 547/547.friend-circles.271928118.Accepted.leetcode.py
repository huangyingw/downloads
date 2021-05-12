class Solution(object):
    def findCircleNum(self, M):
        def dfs(i):
            for j in range(len(M)):
                if M[i][j] == 1:
                    if j not in seen:
                        seen.add(j)
                        dfs(j)
        circles = 0
        seen = set()
        for i in range(len(M)):
            if i not in seen:
                circles += 1
                dfs(i)
        return circles


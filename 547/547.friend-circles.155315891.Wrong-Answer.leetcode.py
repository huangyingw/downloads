class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def find_set(x):
            if set[x] != x:
                set[x] = find_set(set[x])  # path compression.
            return set[x]

        def union_set(x, y):
            x_root, y_root = find_set(x), find_set(y)

        number = len(M)
        set = range(len(M))
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j]:
                    if find_set(i) != find_set(j):
                        union_set(i, j)
                        number -= 1
        return number


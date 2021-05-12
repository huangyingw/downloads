class Solution(object):
    def validTree(self, n, edges):
        uf = self.UnionFind([], n)

        for i in range(0, len(edges)):
            if not uf.union(edges[i][0], edges[i][1]):
                return False

        return uf.count() == 1

    class UnionFind:

        def __init__(self, ids, cnt):
            self.ids = ids
            self.cnt = cnt

        def UnionFind(self, size):
            self.ids = [0 for _ in range(size)]

            for i in range(0, len(self.ids)):
                self.ids[i] = i

            self.cnt = size

        def union(self, m, n):
            src = self.find(m)
            dst = self.find(n)

            if src != dst:
                for i in range(0, len(self.ids)):
                    if self.ids[i] == src:
                        self.ids[i] = dst

                self.cnt -= 1
                return True
            else:
                return False

        def find(self, m):
            return self.ids[m]

        def areConnected(self, m, n):
            return self.find(m) == self.find(n)

        def count(self):
            return self.cnt


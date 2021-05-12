class Solution:
    def wordSubsets(self, A, B):
        uni = collections.Counter()
        for b in B:
            for c, n in collections.Counter(b).items():
                uni[c] = max(uni[c], n)
        res = []
        for a in A:
            count = collections.Counter(a)
            if all(count[c] >= uni[c] for c in uni):
                res.append(a)
        return res


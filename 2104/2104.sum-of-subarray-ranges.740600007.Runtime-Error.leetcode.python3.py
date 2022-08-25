def subArrayRanges(self, A):
    res = 0
    n = len(A)
    for i in xrange(n):
        l, r = A[i], A[i]
        for j in xrange(i, n):
            l = min(l, A[j])
            r = max(r, A[j])
            res += r - l
    return res


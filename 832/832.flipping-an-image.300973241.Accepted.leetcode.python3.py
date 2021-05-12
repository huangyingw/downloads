class Solution(object):
    def flipAndInvertImage(self, A):
        for a in A:
            l, r = 0, len(a) - 1
            while l <= r:
                if a[l] == a[r]:
                    a[l], a[r] = a[l] ^ 1, a[r] ^ 1
                l += 1
                r -= 1
        return A


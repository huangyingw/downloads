class Solution(object):
    def numSpecialEquivGroups(self, A):

        B = set()
        for s in A:
            a, b = s[::2], s[1::2]
            B.add((''.join(sorted(a)), ''.join(sorted(b))))

        return len(B)


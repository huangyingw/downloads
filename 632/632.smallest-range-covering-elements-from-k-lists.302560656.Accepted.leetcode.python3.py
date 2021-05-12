class Solution:
    def smallestRange(self, A):
        import functools
        A = [row[::-1] for row in A]
        ans = -1e9, 1e9
        for left in sorted(functools.reduce(set.union, map(set, A))):
            right = -1e9
            for B in A:
                while B and B[-1] < left:
                    B.pop()
                if not B:
                    return ans
                right = max(right, B[-1])
            if right - left < ans[1] - ans[0]:
                ans = left, right
        return ans


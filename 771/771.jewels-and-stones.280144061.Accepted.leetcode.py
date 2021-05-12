class Solution(object):
    def numJewelsInStones(self, J, S):
        if not J or not S:
            return 0
        j_set = set(J)
        ans = 0
        for c in S:
            if c in j_set:
                ans += 1
        return ans


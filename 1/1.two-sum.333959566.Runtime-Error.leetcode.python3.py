class Solution:

    def firstBadVersion(self, n):
        MAX = n
        MIN = 1

        while MAX >= MIN:
            MID = (MAX + MIN) // 2

            if isBadVersion(MID):
                MAX = MID - 1

            else:
                MIN = MID + 1

        return MAX + 1


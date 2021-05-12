class Solution(object):
    def hIndex(self, citations):
        if not citations:
            return 0

        citations.sort()

        for idx in range(len(citations) - 1, -1, -1):
            if citations[idx] <= len(citations) - idx:
                return citations[idx]


class Solution(object):
    def hIndex(self, citations):
        if not citations:
            return 0
        if len(citations) == 1:
            return 1
        citations.sort()
        for idx in range(len(citations) - 1, -1, -1):
            if citations[idx] <= len(citations) - idx:
                return citations[idx]


class Solution(object):
    def hIndex(self, citations):
        result = 0

        citations.sort(reverse=True)

        for idx in range(citations):
            result = min(idx + 1, citations[idx])

        return result


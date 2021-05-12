class Solution(object):
    def hIndex(self, citations):
        result = 0

        citations.sort(reverse=True)

        for idx, val in enumerate(citations):
            result = max(result, min(idx + 1, val))

        return result


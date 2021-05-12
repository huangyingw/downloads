class Solution(object):
    def hIndex(self, citations):
        result = 0

        for idx, val in enumerate(citations):
            result = max(result, min(len(citations) - idx, val))

        return result


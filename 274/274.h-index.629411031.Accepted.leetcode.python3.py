class Solution(object):
    def hIndex(self, citations):
        result = 0
        citations.sort(reverse=True)
        for idx in range(len(citations)):
            print("idx + 1 --> %s" % (idx + 1))
            print("citations[idx] --> %s" % citations[idx])
            result = max(result, min(idx + 1, citations[idx]))
            print("result --> %s" % result)
        return result


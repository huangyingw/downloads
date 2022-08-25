class Solution(object):
    def hIndex(self, citations):
        result = 0
        citations.sort(reverse=True)
        for idx in range(len(citations)):
            pprint("idx + 1 --> %s" % idx + 1)
            pprint("citations[idx] --> %s" % citations[idx])
            result = min(idx + 1, citations[idx])
        return result


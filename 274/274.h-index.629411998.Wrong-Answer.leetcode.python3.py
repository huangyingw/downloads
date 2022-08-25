class Solution(object):
    def hIndex(self, citations):
        result = 0
        citations.sort(reverse=True)
        for idx, val in enumerate(citations):
            print("idx --> %s" % idx)
            print("val --> %s" % val)
            result = min(idx + 1, val)
            print("result --> %s" % result)
        return result


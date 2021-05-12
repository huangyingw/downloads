class Solution(object):
    def reverseStr(self, s, k):
        reverse = True
        result = []
        for i in range(0, len(s), k):
            block = s[i:i + k]
            if reverse:
                result.append(block[::-1])
            else:
                result.append(block)
            reverse = not reverse
        return "".join(result)


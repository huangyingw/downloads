class Solution(object):
    def xorQueries(self, arr, queries):

        xor = [0]
        for num in arr:
            xor.append(xor[-1] ^ num)
        result = []
        for start, end in queries:
            result.append(xor[end + 1] ^ xor[start])
        return result


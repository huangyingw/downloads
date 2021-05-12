class Solution:
    def frequencySort(self, s: str) -> str:
        d1, d2 = {}, {}
        for c in s:
            d1[c] = d1.get(c, 0) + 1

        for k, v in d1.items():
            d2[v] = d2.get(v, '') + k * v

        res = ''
        for i in range(len(s), -1, -1):
            if i in d2:
                res += d2[i]
        return res

